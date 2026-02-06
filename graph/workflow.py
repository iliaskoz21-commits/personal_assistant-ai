import sqlite3
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from .state import AgentState
from .nodes import weather_node, health_agent, culture_agent, news_agent

def router(state: AgentState):
    """
    Routes the flow to the appropriate node based on user keywords.
    """
    if not state.get("messages"):
        return END
        
    last_message = state["messages"][-1]["content"].lower()
    
    if "weather" in last_message:
        return "weather"
    elif "health" in last_message or "medical" in last_message:
        return "health"
    elif "culture" in last_message or "music" in last_message:
        return "culture"
    elif "news" in last_message:
        return "news"
    
    return END

def create_graph():
    """
    Constructs the LangGraph workflow and initializes SQLite memory.
    """
    builder = StateGraph(AgentState)

    # Define Nodes
    builder.add_node("weather", weather_node)
    builder.add_node("health", health_agent)
    builder.add_node("culture", culture_agent)
    builder.add_node("news", news_agent)

    # Set Conditional Entry Point
    builder.set_conditional_entry_point(
        router,
        {
            "weather": "weather",
            "health": "health",
            "culture": "culture",
            "news": "news",
            END: END
        }
    )

    # Define Edges
    builder.add_edge("weather", END)
    builder.add_edge("health", END)
    builder.add_edge("culture", END)
    builder.add_edge("news", END)

    # FIX for TypeError: Invalid checkpointer
    # We manually open the connection to bypass the Context Manager issue in Python 3.14
    db_path = "./database/memory.db"
    conn = sqlite3.connect(db_path, check_same_thread=False)
    
    # Initialize the saver with the active connection
    memory = SqliteSaver(conn)
    
    # Compile the graph with the valid checkpointer instance
    return builder.compile(checkpointer=memory)
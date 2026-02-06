import gradio as gr
import os
from graph import create_graph

# Ensure database directory exists for SQLite memory
os.makedirs("./database", exist_ok=True)

# Initialize the LangGraph application
app = create_graph()

def chat_fn(message, history, city, username):
    """
    Main chat function that triggers the AI agent workflow.
    """
    # Create a unique thread_id for state persistence
    config = {"configurable": {"thread_id": f"user_{username.strip().lower()}"}}
    
    # Input schema for the graph
    inputs = {
        "messages": [{"role": "user", "content": message}], 
        "city": city
    }
    
    # Invoke the graph and get the response
    output = app.invoke(inputs, config)
    
    # Extract and return the final assistant response
    return output["messages"][-1]["content"]

# Modern Gradio UI Layout
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Multi-Agent Personal Assistant")
    
    with gr.Row():
        with gr.Column(scale=1):
            user_box = gr.Textbox(label="User Name", value="Guest")
            city_box = gr.Textbox(label="Current City", value="Athens")
        
        with gr.Column(scale=3):
            # FIX: Examples must match the number of inputs (message + city + username)
            gr.ChatInterface(
                fn=chat_fn,
                additional_inputs=[city_box, user_box],
                examples=[
                    ["How is the weather?", "Athens", "Guest"],
                    ["Give me health news.", "London", "Guest"],
                    ["Any music events?", "Berlin", "Guest"],
                    ["Global news updates.", "New York", "Guest"]
                ]
            )

if __name__ == "__main__":
    # Theme configuration moved to launch() for Gradio 6.0 compatibility
    demo.launch(theme=gr.themes.Soft())
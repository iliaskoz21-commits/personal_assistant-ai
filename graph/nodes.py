from utils import get_llm, get_search_tool

# Initialize LLM and Search Tool
llm = get_llm()
search_tool = get_search_tool()

def weather_node(state):
    """
    Fetches weather data and formats it into a Markdown table.
    """
    city = state.get("city", "Athens")
    query = f"current weather conditions and 24h forecast in {city} February 2026"
    
    # Fetch raw data
    raw_results = search_tool.invoke(query)
    
    # Prompt for structured output
    prompt = (
        f"Extract weather information for {city} from the following data: {raw_results}. "
        f"Create a Markdown table with metrics: Temperature, Humidity, Wind, and Conditions. "
        f"If there are any alerts (like African dust or storms), list them below the table. "
        f"Answer in a friendly, professional tone."
    )
    
    response = llm.invoke(prompt)
    return {"messages": [{"role": "assistant", "content": response}]}

def health_agent(state):
    """
    Analyzes health news and presents breakthroughs in bullet points.
    """
    query = "latest cancer research breakthroughs and nutrition news February 2026"
    raw_data = search_tool.invoke(query)
    
    prompt = (
        f"Review these health search results: {raw_data}. "
        f"Provide a structured summary using the following format:\n"
        f"1. **Cancer Research Highlights** (Bullet points)\n"
        f"2. **Nutrition & Wellness Tips** (Bullet points)\n"
        f"Focus only on the most recent findings from 2026."
    )
    
    response = llm.invoke(prompt)
    return {"messages": [{"role": "assistant", "content": response}]}

def culture_agent(state):
    """
    Finds cultural events and lists them by category.
    """
    city = state.get("city", "Athens")
    query = f"upcoming music concerts and festivals in {city} February 2026"
    raw_data = search_tool.invoke(query)
    
    prompt = (
        f"Identify music events and festivals in {city} from these results: {raw_data}. "
        f"Organize the output as a Markdown list. Include the Date, Event Name, and Venue if available. "
        f"If no specific events are found, suggest popular cultural hubs in {city}."
    )
    
    response = llm.invoke(prompt)
    return {"messages": [{"role": "assistant", "content": response}]}

def news_agent(state):
    """
    Summarizes global conflicts and environmental news in a 'News Flash' format.
    """
    query = "global conflict updates and climate change environment news February 2026"
    raw_data = search_tool.invoke(query)
    
    prompt = (
        f"Acting as a news analyst, summarize the most critical updates from: {raw_data}. "
        f"Use a 'News Flash' style with bold headings for:\n"
        f"- **Geopolitical Conflicts**\n"
        f"- **Environmental & Climate Updates**\n"
        f"Keep it concise and objective."
    )
    
    response = llm.invoke(prompt)
    return {"messages": [{"role": "assistant", "content": response}]}
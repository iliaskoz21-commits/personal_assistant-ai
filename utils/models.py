import os
from dotenv import load_dotenv
# Using the updated OllamaLLM for LangChain 0.3+ compatibility
from langchain_ollama import OllamaLLM
# Using the stable community path for Tavily Search
from langchain_community.tools.tavily_search import TavilySearchResults

# Load environment variables from the .env file
load_dotenv()

def get_llm():
    """
    Returns the local Mistral model via Ollama.
    The Ollama service must be running locally with the mistral model pulled.
    """
    return OllamaLLM(model="mistral")

def get_search_tool():
    """
    Returns the Tavily Search tool.
    This tool allows agents to perform real-time web searches.
    Requires TAVILY_API_KEY to be set in the .env file.
    """
    # k=5 limits the results to the top 5 most relevant links
    return TavilySearchResults(k=5)
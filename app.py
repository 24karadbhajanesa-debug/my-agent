import config
from tavily import TavilyClient

def search_medicine_info(query: str):
    """
    Search for information about a specific medicine.
    """
    if not config.TAVILY_API_KEY:
        return [{"title": "Notice", "content": "Tavily API key missing. Search disabled."}]
    
    tavily = TavilyClient(api_key=config.TAVILY_API_KEY)
    response = tavily.search(query=query, search_depth="advanced")
    return response['results']

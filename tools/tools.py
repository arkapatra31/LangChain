from langchain_community.tools.tavily_search import TavilySearchResults
import json


def get_profile_tavily(name: str):
    try:
        """Searches for LinkedIn or Twitter Profile Page."""
        search = TavilySearchResults()
        res = search.run(f"{name}")
        print(json.dumps(res, indent=4))
        return res[0]  # ["url"]
    except Exception as ex:
        print(ex)
        raise Exception(ex)


__all__ = [
    get_profile_tavily
]

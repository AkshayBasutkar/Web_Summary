import logging
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)

def get_top_urls_from_keyword(keyword: str, api_key: str, cse_id: str, num_results: int = 10) -> list:
    """
    Fetch top URLs from Google Custom Search API for a given keyword.

    Args:
        keyword (str): The keyword or phrase to search for.
        api_key (str): The Google API key entered by user.
        cse_id (str): The Custom Search Engine ID entered by user.
        num_results (int): Number of URLs to fetch (default: 10).

    Returns:
        list: A list of URLs.
    """
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=keyword, cx=cse_id, num=num_results).execute()
        items = res.get("items", [])
        urls = [item["link"] for item in items if "link" in item]
        logger.info(f"✅ Found {len(urls)} URLs for keyword: {keyword}")
        return urls
    except Exception as e:
        logger.error(f"❌ Failed to fetch URLs for '{keyword}': {e}")
        return []

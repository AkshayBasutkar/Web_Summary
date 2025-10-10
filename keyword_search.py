# keyword_search.py
import os
import logging
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

CSE_ID = os.getenv("GOOGLE_CSE_ID")
API_KEY = os.getenv("GOOGLE_API_KEY")

def get_top_urls_from_keyword(keyword: str, num_results: int = 10) -> list:
    """Fetch top URLs from Google Custom Search for a keyword."""
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        res = service.cse().list(q=keyword, cx=CSE_ID, num=num_results).execute()
        items = res.get("items", [])
        urls = [item["link"] for item in items]
        logger.info(f"✅ Found {len(urls)} URLs for keyword: {keyword}")
        return urls
    except Exception as e:
        logger.error(f"❌ Failed to fetch URLs for '{keyword}': {e}")
        return []

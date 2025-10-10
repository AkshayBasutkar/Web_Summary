import logging
import trafilatura
from config import DOCS_DIR, ALLOWED_EXTENSIONS
from modules.preprocessor import clean_text, preprocess_text
from modules.utils import save_text_to_file

# ============================================================
# 🔹 TEXT EXTRACTION MODULE
# ============================================================

def get_and_preprocess_text(url: str) -> str:
    """
    Fetches, extracts, and preprocesses main text content from a URL.

    Steps:
    1. Fetch the web page content.
    2. Extract main text using Trafilatura.
    3. Clean and normalize text using preprocessor module.

    Args:
        url (str): URL of the webpage to extract text from.

    Returns:
        str: Cleaned text if extraction succeeds, else None.
    """
    logging.info(f"🌐 Fetching content from URL: {url}")
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            logging.warning(f"Failed to download content from: {url}")
            return None

        extracted = trafilatura.extract(downloaded, include_links=False)
        if not extracted:
            logging.warning(f"Trafilatura failed to extract content from: {url}")
            return None

        # Clean and preprocess text
        cleaned = clean_text(extracted)
        processed = preprocess_text(cleaned)

        logging.info(f"✅ Successfully extracted and preprocessed text from: {url}")
        return processed

    except Exception as e:
        logging.exception(f"Error during extraction from {url}: {e}")
        return None


def save_extracted_text(text: str, filename: str = "extracted_text") -> str:
    """
    Saves extracted text to the DOCS_DIR folder.

    Args:
        text (str): Text content to save.
        filename (str): Prefix for saved file.

    Returns:
        str: Full path to saved file.
    """
    try:
        path = save_text_to_file(text, folder=DOCS_DIR, prefix=filename)
        return path
    except Exception as e:
        logging.exception(f"Failed to save extracted text: {e}")
        return ""


def is_allowed_file(file_name: str) -> bool:
    """
    Checks if a file has an allowed extension.

    Args:
        file_name (str): Name of the file to check.

    Returns:
        bool: True if allowed, False otherwise.
    """
    return any(file_name.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)

import logging
import requests
from bs4 import BeautifulSoup
from readability import Document
import re
from config import (
    DOCS_DIR, 
    ALLOWED_EXTENSIONS,
    EXTRACTION_TIMEOUT,
    USER_AGENT,
    NOISE_TAGS,
    ALLOWED_CONTENT_TAGS,
    TABLE_DATA_LABEL
)
from modules.preprocessor import clean_text, preprocess_text
from modules.utils import save_text_to_file


class WebTextExtractor:

    def __init__(self, url, timeout=None, user_agent=None):
        self.url = url
        self.timeout = timeout if timeout is not None else EXTRACTION_TIMEOUT
        self.headers = {
            "User-Agent": user_agent if user_agent else USER_AGENT
        }

    def fetch_html(self):
        try:
            response = requests.get(
                self.url,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch page: {e}")

    def extract_main_content(self, html):
        try:
            doc = Document(html)
            return doc.summary(html_partial=True)
        except Exception:
            return html

    def remove_noise(self, soup):
        """Remove noise tags from HTML soup using configured noise tags."""
        # Strip whitespace from tag names
        noise_tags = [tag.strip() for tag in NOISE_TAGS if tag.strip()]
        
        for tag in soup.find_all(noise_tags):
            tag.decompose()

        return soup

    def normalize_text(self, text):
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def extract_content(self, soup):
        """Extract content from HTML soup using configured allowed tags."""
        extracted = []
        seen = set()

        # Strip whitespace from tag names
        allowed_tags = [tag.strip() for tag in ALLOWED_CONTENT_TAGS if tag.strip()]

        for element in soup.find_all(allowed_tags):
            text = element.get_text(separator=" ", strip=True)

            if not text:
                continue

            text = self.normalize_text(text)

            key = text.lower()
            if key in seen:
                continue

            seen.add(key)

            tag_name = element.name

            if tag_name.startswith("h"):
                extracted.append(f"\n{text.upper()}\n")
            elif tag_name == "li":
                extracted.append(f"- {text}")
            elif tag_name in ["td", "th"]:
                extracted.append(text)
            else:
                extracted.append(text)

        return extracted

    def format_tables(self, soup):
        tables_text = []

        for table in soup.find_all("table"):
            for row in table.find_all("tr"):
                cells = row.find_all(["th", "td"])
                row_text = " | ".join(
                    self.normalize_text(cell.get_text())
                    for cell in cells if cell.get_text(strip=True)
                )
                if row_text:
                    tables_text.append(row_text)

        return tables_text

    def extract(self):
        html = self.fetch_html()
        main_html = self.extract_main_content(html)

        soup = BeautifulSoup(main_html, "lxml")
        soup = self.remove_noise(soup)

        main_text = self.extract_content(soup)
        table_text = self.format_tables(soup)

        final_output = []

        if main_text:
            final_output.extend(main_text)

        if table_text:
            final_output.append(TABLE_DATA_LABEL)
            final_output.extend(table_text)

        return "\n\n".join(final_output)


# TEXT EXTRACTION MODULE - Public API Functions

def get_and_preprocess_text(url: str) -> str:
    """
    Fetches, extracts, and preprocesses main text content from a URL.

    Steps:
    1. Fetch the web page content.
    2. Extract main text using WebTextExtractor (readability + BeautifulSoup).
    3. Clean and normalize text using preprocessor module.

    Args:
        url (str): URL of the webpage to extract text from.

    Returns:
        str: Cleaned text if extraction succeeds, else None.
    """
    logging.info(f"🌐 Fetching content from URL: {url}")
    try:
        extractor = WebTextExtractor(url)
        extracted = extractor.extract()
        
        if not extracted or not extracted.strip():
            logging.warning(f"Failed to extract content from: {url}")
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



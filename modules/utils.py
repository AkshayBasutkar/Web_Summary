import os
import logging
from datetime import datetime
from config import LOGS_DIR, LOG_FILE, DATA_DIR
from config import DOCUMENTS_DIR, OUTPUTS_DIR

# ============================================================
# 🔹 LOGGING SETUP
# ============================================================

logger = logging.getLogger(__name__)

def setup_logging():
    """
    Configures logging for the entire project.
    Logs are written both to console and to a file (rag_pipeline.log).
    """
    os.makedirs(LOGS_DIR, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logging.info("🧩 Logging initialized successfully.")


# ============================================================
# 🔹 HELPER FUNCTIONS
# ============================================================

def timestamp() -> str:
    """Returns current timestamp as string."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def save_extracted_text(text: str, filename: str = None) -> str:
    """
    Saves the extracted article text to a file.
    Returns the full file path.
    """
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"extracted_article_{timestamp}.txt"
    filepath = os.path.join(DOCUMENTS_DIR, filename)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        logger.info(f"📝 Extracted text saved: {filepath}")
    except Exception as e:
        logger.error(f"❌ Failed to save extracted text: {e}")
    
    return filepath


def save_text_to_file(
    content: str, 
    folder: str = os.path.join(DATA_DIR, "outputs"), 
    prefix: str = "output"
) -> str:
    """
    Saves text content to a file with timestamped name.

    Args:
        content (str): Text to save.
        folder (str): Directory where file will be saved.
        prefix (str): Prefix for the file name.

    Returns:
        str: Full path of the saved file.
    """
    try:
        os.makedirs(folder, exist_ok=True)
        filename = f"{prefix}_{timestamp()}.txt"
        path = os.path.join(folder, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"📝 File saved successfully: {path}")
        return path
    except Exception as e:
        logging.exception(f"Failed to save file: {e}")
        return ""


def read_text_file(file_path: str) -> str:
    """
    Reads a text file safely and returns content.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: File content or empty string if error occurs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logging.exception(f"Failed to read file {file_path}: {e}")
        return ""

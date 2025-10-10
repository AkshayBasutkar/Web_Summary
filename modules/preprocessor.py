import re
import logging

# ============================================================
# 🔹 TEXT PREPROCESSING MODULE
# ============================================================

def clean_text(text: str) -> str:
    """
    Basic cleaning of raw text:
    - Removes HTML entities (&nbsp;, &amp;)
    - Replaces multiple whitespace/newlines with single space
    - Removes non-printable/control characters
    """
    try:
        logging.info("🧹 Starting basic text cleaning...")
        # Remove HTML entities
        text = re.sub(r"&[a-zA-Z]+;", " ", text)
        # Replace multiple spaces, tabs, newlines with single space
        text = re.sub(r"\s+", " ", text)
        # Remove control/non-printable characters
        text = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", text)
        text = text.strip()
        logging.info("✅ Text cleaning completed.")
        return text
    except Exception as e:
        logging.exception(f"Error during clean_text: {e}")
        return text


def preprocess_text(
    text: str, 
    lowercase: bool = True, 
    remove_numbers: bool = False
) -> str:
    """
    Additional preprocessing steps:
    - Optional lowercase conversion
    - Optional number removal
    - Minor punctuation spacing normalization
    """
    try:
        logging.info("🧩 Starting advanced text preprocessing...")
        processed = text

        if lowercase:
            processed = processed.lower()
        if remove_numbers:
            processed = re.sub(r"\d+", "", processed)
        # Normalize spaces before punctuation
        processed = re.sub(r'\s([?.!,"])', r'\1', processed)
        processed = processed.strip()

        logging.info("✅ Advanced preprocessing completed.")
        return processed
    except Exception as e:
        logging.exception(f"Error during preprocess_text: {e}")
        return text


def basic_preprocess_pipeline(text: str) -> str:
    """
    Runs a combined pipeline: clean_text -> preprocess_text
    Use this in extractor.py to get fully processed text
    """
    text = clean_text(text)
    text = preprocess_text(text)
    return text

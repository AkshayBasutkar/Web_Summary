# modules/summarizer.py

import logging
from config import GEMINI_MODEL_NAME, GEMINI_API_KEY
import google.generativeai as genai

# -------------------------------
# Setup logging
# -------------------------------
logger = logging.getLogger(__name__)

# -------------------------------
# Summarization Function
# -------------------------------
def summarize_text(text: str, summary_type: str = "concise", custom_instructions: str = None) -> str:
    """
    Summarizes the given text using Google Gemini model.

    Args:
        text (str): The input text to summarize.
        summary_type (str): 'concise', 'detailed', or 'key_points'.
        custom_instructions (str, optional): Custom instructions to guide the AI model.

    Returns:
        str: The summarized text.
    """
    try:
        # Configure API key
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL_NAME)
        logger.info(f"📝 Summarizing text using model: {GEMINI_MODEL_NAME}, type: {summary_type}")

        # Build prompt
        if custom_instructions:
            prompt = f"{custom_instructions}\n\n{text}"
        else:
            prompt = f"Please summarize the following text in a {summary_type} style:\n\n{text}"

        # Generate summary
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                max_output_tokens=20000,
                temperature=0.3
            )
        )

        summary_text = response.text.strip()
        logger.info(f"✅ Summarization completed. Summary length: {len(summary_text)} characters")
        return summary_text

    except Exception as e:
        logger.error(f"❌ Error during summarization: {e}")
        return "Error: Summarization failed."

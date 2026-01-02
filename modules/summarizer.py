import logging
import google.generativeai as genai

# Setup logging
logger = logging.getLogger(__name__)

def summarize_text(text: str, gemini_api_key: str, summary_type: str = "Short Summary", custom_instructions: str = None) -> str:
    """
    Summarizes the given text using Google Gemini model.

    Args:
        text (str): The input text to summarize.
        gemini_api_key (str): The Gemini API key entered by the user.
        summary_type (str): 'Short Summary', 'Detailed Summary', or 'Bullet Points'.
        custom_instructions (str, optional): Custom user-provided summarization style.

    Returns:
        str: The summarized text.
    """
    try:
        # Configure Gemini API dynamically
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-flash-lite-latest")
        logger.info(f"🧠 Using Gemini model for {summary_type} summarization")

        # Define prompt based on summary type
        if custom_instructions:
            prompt = f"{custom_instructions}\n\n{text}"
        elif summary_type == "Short Summary":
            prompt = f"Summarize the following text in 3–4 sentences, keeping it concise and clear:\n\n{text}"
        elif summary_type == "Detailed Summary":
            prompt = f"Provide a detailed paragraph-wise summary of the following text:\n\n{text}"
        elif summary_type == "Bullet Points":
            prompt = f"Summarize the following text into well-structured, concise bullet points:\n\n{text}"
        else:
            prompt = f"Provide a concise summary of the following text:\n\n{text}"

        # Generate summary
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                max_output_tokens=20000,
                temperature=0.3
            )
        )

        # Extract and clean output
        summary_text = response.text.strip()
        logger.info(f"✅ Summarization completed (Length: {len(summary_text)} chars)")
        return summary_text

    except Exception as e:
        logger.error(f"❌ Error during summarization: {e}")
        return "⚠️ Error: Summarization failed. Please check your API key or try again."
import streamlit as st
from modules.extractor import get_and_preprocess_text
from modules.summarizer import summarize_text

def app():
    st.title("🔹 URL Summarizer")
    st.write(
        """
        Enter one or more URLs (one per line) to extract and summarize their content.
        You can also choose the summary type and optionally provide custom instructions for the AI model.
        """
    )

    # --- Get API Key ---
    gemini_key = st.session_state.get("GEMINI_API_KEY")
    if not gemini_key:
        st.warning("❌ Gemini API key not set. Go to Home page to enter API keys.")
        return

    # --- Input Fields ---
    urls_input = st.text_area("Enter URLs (one per line):", height=150)
    urls = [url.strip() for url in urls_input.splitlines() if url.strip()]
    
    summary_type = st.selectbox(
        "Select summary type:",
        options=["concise", "detailed", "key_points"]
    )
    
    custom_instructions = st.text_area(
        "Optional: Custom instructions for the AI model",
        height=100
    )

    if st.button("Summarize URLs"):
        if not urls:
            st.warning("⚠️ Please enter at least one URL.")
            return

        for i, url in enumerate(urls, 1):
            st.info(f"🌐 Processing URL {i}: {url}")
            
            text = get_and_preprocess_text(url)
            if not text:
                st.error(f"Failed to extract text from: {url}")
                continue

            # --- Collapsible extracted text ---
            with st.expander(f"📄 Extracted Text {i}"):
                st.text_area("", text, height=150, key=f"extracted_{i}")

            # --- Summarize ---
            summary = summarize_text(
                text,
                summary_type=summary_type,
                custom_instructions=custom_instructions,
                gemini_api_key=gemini_key
            )

            # --- Collapsible summary ---
            with st.expander(f"📝 Summary {i}"):
                st.text_area("", summary, height=150, key=f"summary_{i}")

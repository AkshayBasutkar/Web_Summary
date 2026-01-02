import streamlit as st
from modules.new_extractor import get_and_preprocess_text
from modules.summarizer import summarize_text
from keyword_search import get_top_urls_from_keyword

def app():
    st.title("🔹 Keyword Summarizer")
    st.write(
        """
        Enter a keyword and fetch the top websites for summarization.
        You can choose the summary type, number of top websites, and optionally provide custom instructions for the AI model.
        """
    )

    # --- Get API Keys ---
    gemini_key = st.session_state.get("GEMINI_API_KEY")
    google_api_key = st.session_state.get("GOOGLE_API_KEY")
    google_cse_id = st.session_state.get("GOOGLE_CSE_ID")

    if not gemini_key or not google_api_key or not google_cse_id:
        st.warning("❌ Please set all API keys in the Home page first.")
        return

    # --- Input Fields ---
    keyword = st.text_input("Enter keyword:")
    num_sites = st.number_input("Number of top websites to fetch:", min_value=1, max_value=10, value=5)
    summary_type = st.selectbox(
        "Select summary type:",
        options=["concise", "detailed", "key_points"]
    )
    custom_instructions = st.text_area(
        "Optional: Custom instructions for the AI model",
        height=100
    )

    if st.button("Fetch & Summarize"):
        if not keyword.strip():
            st.warning("⚠️ Please enter a keyword.")
            return

        # --- Fetch Top URLs ---
        urls = get_top_urls_from_keyword(
            keyword=keyword,
            num_results=num_sites,
            api_key=google_api_key,
            cse_id=google_cse_id
        )

        if not urls:
            st.error("❌ No URLs found for this keyword.")
            return

        for i, url in enumerate(urls, 1):
            st.info(f"🌐 Processing URL {i}: {url}")

            text = get_and_preprocess_text(url)
            if not text:
                st.error(f"Failed to extract text from: {url}")
                continue

            # --- Collapsible extracted text ---
            with st.expander(f"📄 Extracted Text {i}"):
                st.text_area("", text, height=150, key=f"kw_extracted_{i}")

            # --- Summarize ---
            summary = summarize_text(
                text,
                summary_type=summary_type,
                custom_instructions=custom_instructions,
                gemini_api_key=gemini_key
            )

            # --- Collapsible summary ---
            with st.expander(f"📝 Summary {i}"):
                st.text_area("", summary, height=150, key=f"kw_summary_{i}")

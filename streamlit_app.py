import streamlit as st

# Import your page modules (make sure each page has an `app()` function)
import pages.home as home_page
import pages.url_summarization as url_page
import pages.keyword_summarization as keyword_page

# --- Page Config ---
st.set_page_config(
    page_title="AI Summarizer",
    page_icon="🧠",
    layout="wide"
)

# --- Sidebar Menu ---
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "URL Summarizer", "Keyword Summarizer"]
)

# --- Render Selected Page ---
if page == "Home":
    home_page.app()
elif page == "URL Summarizer":
    url_page.app()
elif page == "Keyword Summarizer":
    keyword_page.app()

# --- Sidebar Footer ---
st.sidebar.markdown("---")
st.sidebar.caption("💡 Built with ❤️ using Streamlit and Gemini API")

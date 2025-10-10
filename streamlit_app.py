import streamlit as st

st.set_page_config(
    page_title="📝 Web Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Web Summarizer")
st.subheader("Summarize web content quickly using AI")

st.markdown("""
Welcome to the **Web Summarizer** app! This tool allows you to extract and summarize content from web pages
or search results using Google Gemini AI.  

You can choose one of the following pages from the sidebar:

1. **Summarize by URL** – Enter one or multiple URLs and optionally provide custom instructions for summarization.  
2. **Summarize by Keyword** – Enter a keyword, and the app will summarize the top 10 search results.  

💡 **Tip:** You can provide custom instructions to tell the AI exactly how you want the summary.
""")

st.image(
    "https://images.unsplash.com/photo-1554774853-87f5d6c28c2f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8c3VtbWFyeXxlbnwwfHx8fDE2OTc3MDk1MzU&ixlib=rb-4.0.3&q=80&w=1080",
    use_container_width=True
)

st.markdown("---")
st.info("Select a page from the sidebar to get started with summarization!")

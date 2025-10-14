import streamlit as st

def app():
    st.title("🏠 AI Summarizer - API Key Setup")
    st.write(
        """
        Please enter all your API credentials below. 
        These keys will be used in other pages to summarize URLs or keywords.
        """
    )

    # --- Input Fields ---
    gemini_key = st.text_input("Enter Gemini API Key:", type="password")
    google_api_key = st.text_input("Enter Google API Key:", type="password")
    google_cse_id = st.text_input("Enter Google CSE ID:")

    # --- Submit Button ---
    if st.button("Save API Keys"):
        if not gemini_key or not google_api_key or not google_cse_id:
            st.warning("⚠️ Please fill in all fields before saving.")
        else:
            # Save keys in session_state
            st.session_state["GEMINI_API_KEY"] = gemini_key
            st.session_state["GOOGLE_API_KEY"] = google_api_key
            st.session_state["GOOGLE_CSE_ID"] = google_cse_id
            st.success("✅ API keys saved successfully! You can now use the other pages.")

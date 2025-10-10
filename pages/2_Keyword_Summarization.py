import streamlit as st
from modules.utils import save_text_to_file, save_extracted_text
from modules.extractor import get_and_preprocess_text
from modules.summarizer import summarize_text
from keyword_search import get_top_urls_from_keyword

st.title("🔹 Summarize by Keyword")
st.write(
    "Enter a keyword. Optionally provide custom instructions for AI summarization.\n"
    "The app will summarize the top 10 search results."
)

keyword = st.text_input("Enter Keyword")
custom_instr_kw = st.text_area("Custom Instructions (Optional)", height=70)
generate_kw_btn = st.button("Generate Summaries (Keyword)")

if generate_kw_btn:
    if not keyword.strip():
        st.error("❌ Please enter a keyword.")
    else:
        urls = get_top_urls_from_keyword(keyword, num_results=10)
        if not urls:
            st.error("❌ No URLs found for this keyword.")
        else:
            all_summaries = []
            for idx, url in enumerate(urls, start=1):
                with st.expander(f"🔹 URL {idx}: {url}", expanded=True):
                    text = get_and_preprocess_text(url)
                    if not text:
                        st.error("❌ Extraction failed")
                        all_summaries.append({"URL": url, "Summary": "Extraction failed"})
                        continue

                    st.text_area("Extracted Text", text, height=200, key=f"kw_extracted_text_{idx}")
                    save_extracted_text(text, filename=f"kw_extracted_article_{idx}")

                    summary = summarize_text(text, custom_instructions=custom_instr_kw)
                    st.text_area("Summary", summary, height=150, key=f"kw_summary_text_{idx}")
                    save_text_to_file(summary, prefix=f"kw_summary_{idx}")

                    all_summaries.append({"URL": url, "Summary": summary})

            if all_summaries:
                combined_text = "\n\n".join([f"URL: {s['URL']}\nSummary: {s['Summary']}\n{'-'*80}" for s in all_summaries])
                st.download_button("📥 Download All Summaries", combined_text, "keyword_summaries.txt", "text/plain")

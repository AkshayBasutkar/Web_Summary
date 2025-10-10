import streamlit as st
from modules.utils import save_text_to_file, save_extracted_text
from modules.extractor import get_and_preprocess_text
from modules.summarizer import summarize_text
from config import DEFAULT_SUMMARY_TYPE

st.title("🔹 Summarize by URL")
st.write(
    "Enter one or multiple URLs. Optionally provide custom instructions for AI summarization.\n"
    "Format per line: `URL | summary_type` (summary_type: concise, detailed, key_points)."
)

urls_input = st.text_area("Enter URLs", height=150)
custom_instr = st.text_area("Custom Instructions (Optional)", height=70)
generate_button = st.button("Generate Summaries (URL)")

SUMMARY_OPTIONS = ["concise", "detailed", "key_points"]

def parse_urls_with_type(text: str):
    entries = []
    for line in text.strip().splitlines():
        if "|" in line:
            url_part, type_part = line.split("|", 1)
            url = url_part.strip()
            summary_type = type_part.strip().lower()
            if url and summary_type in SUMMARY_OPTIONS:
                entries.append({"url": url, "summary_type": summary_type})
        else:
            url = line.strip()
            if url:
                entries.append({"url": url, "summary_type": DEFAULT_SUMMARY_TYPE})
    return entries

if generate_button:
    entries = parse_urls_with_type(urls_input)
    if not entries:
        st.error("❌ Please enter at least one valid URL.")
    else:
        all_summaries = []
        for idx, entry in enumerate(entries, start=1):
            url = entry["url"]
            summary_type = entry["summary_type"]

            with st.expander(f"🔹 URL {idx}: {url} ({summary_type})", expanded=True):
                text = get_and_preprocess_text(url)
                if not text:
                    st.error("❌ Extraction failed")
                    all_summaries.append({"URL": url, "Summary": "Extraction failed"})
                    continue

                st.text_area("Extracted Text", text, height=200, key=f"url_extracted_text_{idx}")
                save_extracted_text(text, filename=f"extracted_article_{idx}")

                summary = summarize_text(text, summary_type, custom_instr)
                st.text_area("Summary", summary, height=150, key=f"url_summary_text_{idx}")
                save_text_to_file(summary, prefix=f"summary_{idx}")

                all_summaries.append({"URL": url, "Summary": summary})

        if all_summaries:
            combined_text = "\n\n".join([f"URL: {s['URL']}\nSummary: {s['Summary']}\n{'-'*80}" for s in all_summaries])
            st.download_button("📥 Download All Summaries", combined_text, "all_summaries.txt", "text/plain")

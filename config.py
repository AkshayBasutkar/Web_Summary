import os
from dotenv import load_dotenv

# --- Load environment variables from .env if available ---
load_dotenv()

# --- Base directories ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(DATA_DIR, "documents")
CHUNKS_DIR = os.path.join(DATA_DIR, "chunks")
VECTOR_DB_DIR = os.path.join(DATA_DIR, "vector_db")
CACHE_DIR = os.path.join(DATA_DIR, "cache")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

DEFAULT_TEMPERATURE=0.3
DEFAULT_MAX_TOKENS=20000
DEFAULT_SUMMARY_TYPE='concise'

# --- Ensure all directories exist ---
for directory in [DATA_DIR, DOCS_DIR, CHUNKS_DIR, VECTOR_DB_DIR, CACHE_DIR, LOGS_DIR]:
    os.makedirs(directory, exist_ok=True)

# --- Model configurations ---
# Use HuggingFace or OpenAI embeddings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")  # replace with your LLM (local or API)

# --- Summarization model (for summarizer.py) ---
SUMMARIZER_MODEL = os.getenv("SUMMARIZER_MODEL", "facebook/bart-large-cnn")

# --- Chunking configurations ---
CHUNK_SIZE = 1000       # Number of characters per chunk
CHUNK_OVERLAP = 100     # Overlap between chunks for better context

# --- File extensions allowed ---
ALLOWED_EXTENSIONS = [".pdf", ".txt", ".docx", ".csv", ".md"]

# --- Vector store type ---
VECTOR_STORE = os.getenv("VECTOR_STORE", "faiss")  # faiss, chroma, or pinecone

# --- OpenAI / HuggingFace API Keys ---
GOOGLE_API_KEY = "AIzaSyCiYhn3fmEu1QT3_sPhmA9Vh7UGijs5tG8"
HF_TOKEN = os.getenv("HF_TOKEN", "")

# --- Logging setup ---
LOG_FILE = os.path.join(LOGS_DIR, "rag_pipeline.log")

# --- Utility constants ---
MAX_RESULTS = 5  # max retrieved chunks per query
DEVICE = "cuda" if os.getenv("USE_CUDA", "false").lower() == "true" else "cpu"

# --- Function for printing current config (debugging) ---
def print_config_summary():
    print("\n🔧 Current Configuration Summary 🔧")
    print(f"Base Directory      : {BASE_DIR}")
    print(f"Embedding Model     : {EMBEDDING_MODEL}")
    print(f"LLM Model           : {LLM_MODEL}")
    print(f"Summarizer Model    : {SUMMARIZER_MODEL}")
    print(f"Vector Store        : {VECTOR_STORE}")
    print(f"Chunk Size          : {CHUNK_SIZE}")
    print(f"Allowed Extensions  : {ALLOWED_EXTENSIONS}")
    print(f"Device              : {DEVICE}")
    print(f"Data Directory      : {DATA_DIR}")
    print("------------------------------------------------\n")


GEMINI_API_KEY = "AIzaSyCiYhn3fmEu1QT3_sPhmA9Vh7UGijs5tG8"
GEMINI_MODEL_NAME = "gemini-2.5-flash"

# -----------------------------
# Default Settings
# -----------------------------
DEFAULT_SUMMARY_TYPE = os.getenv("DEFAULT_SUMMARY_TYPE", "concise")

# -----------------------------
# Paths for saving files
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCUMENTS_DIR = os.path.join(BASE_DIR, "data", "documents")
OUTPUTS_DIR = os.path.join(BASE_DIR, "data", "outputs")

# Create directories if they don't exist
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

if __name__ == "__main__":
    print_config_summary()

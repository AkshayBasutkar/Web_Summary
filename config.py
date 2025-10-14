import os
from dotenv import load_dotenv

# --- Load environment variables from .env if available ---
load_dotenv()

DEFAULT_TEMPERATURE=0.3
DEFAULT_MAX_TOKENS=20000
DEFAULT_SUMMARY_TYPE='concise'

# --- Model configurations ---
# Use HuggingFace  embeddings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")


# --- File extensions allowed ---
ALLOWED_EXTENSIONS = [".pdf", ".txt", ".docx", ".csv", ".md"]


# --- Gemini / HuggingFace API Keys ---
GEMINI_API_KEY = "AIzaSyCiYhn3fmEu1QT3_sPhmA9Vh7UGijs5tG8"
GEMINI_MODEL_NAME = "gemini-2.5-flash"


# --- Logging setup ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOGS_DIR, "rag_pipeline.log")
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(DATA_DIR, "documents")

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


import os
from dotenv import load_dotenv

# --- Load environment variables from .env if available ---
load_dotenv()

# -----------------------------
# Base Directory Setup
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------
# Paths Configuration
# -----------------------------
LOGS_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOGS_DIR, "rag_pipeline.log")
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(DATA_DIR, "documents")
DOCUMENTS_DIR = os.path.join(DATA_DIR, "documents")
OUTPUTS_DIR = os.path.join(DATA_DIR, "outputs")

# Create directories if they don't exist
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# -----------------------------
# Gemini AI Configuration
# -----------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")  # Should be set via UI or .env
# Use gemini-1.5-flash for better free tier support (gemini-2.0-flash-exp has limited/no free tier)
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-flash")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.3"))
DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", "20000"))

# Retry configuration for rate limit errors
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
RETRY_DELAY_BASE = float(os.getenv("RETRY_DELAY_BASE", "2.0"))  # Base delay in seconds

# -----------------------------
# Summary Configuration
# -----------------------------
DEFAULT_SUMMARY_TYPE = os.getenv("DEFAULT_SUMMARY_TYPE", "concise")
SUMMARY_TYPE_MAPPING = {
    "concise": "Short Summary",
    "detailed": "Detailed Summary",
    "key_points": "Bullet Points"
}

# -----------------------------
# Web Extraction Configuration
# -----------------------------
EXTRACTION_TIMEOUT = int(os.getenv("EXTRACTION_TIMEOUT", "15"))
USER_AGENT = os.getenv(
    "USER_AGENT",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

# HTML tags to remove during extraction (noise removal)
NOISE_TAGS = os.getenv(
    "NOISE_TAGS",
    "script,style,nav,footer,header,aside,noscript,iframe,form,button"
).split(",")

# HTML tags to extract content from
ALLOWED_CONTENT_TAGS = os.getenv(
    "ALLOWED_CONTENT_TAGS",
    "h1,h2,h3,h4,h5,h6,p,li,td,th"
).split(",")

# Table data label
TABLE_DATA_LABEL = os.getenv("TABLE_DATA_LABEL", "\nTABLE DATA\n")

# -----------------------------
# File Extensions Configuration
# -----------------------------
ALLOWED_EXTENSIONS = os.getenv(
    "ALLOWED_EXTENSIONS",
    ".pdf,.txt,.docx,.csv,.md"
).split(",")

# -----------------------------
# Embedding Model Configuration (if needed)
# -----------------------------
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")


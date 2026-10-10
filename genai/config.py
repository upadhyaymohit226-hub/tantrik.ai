import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")
    LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.1-70b-versatile")
    EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    CHROMA_DIR = "chroma_db"
    COLLECTION_NAME = "job_skill_docs"
    TOP_K = 4

config = Config()

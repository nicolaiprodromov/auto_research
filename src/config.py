import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL", "https://api.tavily.com/v1/search")

PAT_TOKEN = os.getenv("PAT_TOKEN")
GITHUB_MODELS_ENDPOINT = os.getenv("GITHUB_MODELS_ENDPOINT", "https://models.inference.ai.azure.com")
GITHUB_MODEL = os.getenv("GITHUB_MODEL", "gpt-4o")

if not API_KEY:
    raise ValueError("API key not found. Please set the API_KEY environment variable.")
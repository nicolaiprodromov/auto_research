import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL", "https://api.tavily.com/v1/search")

if not API_KEY:
    raise ValueError("API key not found. Please set the API_KEY environment variable.")
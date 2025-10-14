import requests
from .config import FIRECRAWL_API_KEY, FIRECRAWL_API_URL

class FirecrawlClient:
    def __init__(self):
        self.api_key = FIRECRAWL_API_KEY
        self.base_url = FIRECRAWL_API_URL
        self.results = []

    def search(self, term, max_results=5):
        if not self.api_key:
            raise ValueError(f"FIRECRAWL_API_KEY not found in environment variables: {self.api_key}")
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "query": term,
            "limit": max_results
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            self.results = response.json()
            return self.results
        except requests.exceptions.RequestException as e:
            print(f"Error during search: {e}")
            return None

    def get_results(self):
        return self.results

import requests
from .config import API_KEY, API_URL

class TavilyClient:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = API_URL
        self.results = []

    def search(self, term, max_results=5):
        if not self.api_key:
            raise ValueError(f"TAVILY_API_KEY not found in environment variables: {self.api_key}")
        
        headers = {"Content-Type": "application/json"}
        payload = {
            "api_key": self.api_key,
            "query": term,
            "max_results": max_results
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

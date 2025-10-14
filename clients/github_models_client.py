import os
from openai import OpenAI

class GitHubModelsClient:
    def __init__(self, token=None, model="gpt-4o"):
        self.token = token or os.environ.get("PAT_TOKEN")
        if not self.token:
            raise ValueError("GitHub token is required. Set PAT_TOKEN environment variable.")
        
        self.model = model
        self.endpoint = "https://models.inference.ai.azure.com"
        self.client = OpenAI(
            base_url=self.endpoint,
            api_key=self.token,
        )
    
    def chat(self, message, system_prompt=None):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": message})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=2000,
        )
        
        return response.choices[0].message.content
    
    def chat_with_history(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=2000,
        )
        
        return response.choices[0].message.content

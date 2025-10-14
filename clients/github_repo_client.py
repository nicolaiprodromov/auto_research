import os
import requests
import base64

class GitHubRepoClient:
    def __init__(self, token=None, owner=None, repo=None):
        self.token = token or os.environ.get("PAT_TOKEN")
        if not self.token:
            raise ValueError("GitHub token is required. Set PAT_TOKEN environment variable.")
        
        self.owner = owner or os.environ.get("GITHUB_OWNER")
        self.repo = repo or os.environ.get("GITHUB_REPO")
        
        if not self.owner or not self.repo:
            raise ValueError("GitHub owner and repo are required. Set GITHUB_OWNER and GITHUB_REPO environment variables.")
        
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def write_file(self, path, content, message=None, branch="main"):
        url = f"{self.base_url}/repos/{self.owner}/{self.repo}/contents/{path}"
        
        sha = None
        response = requests.get(url, headers=self.headers, params={"ref": branch})
        if response.status_code == 200:
            sha = response.json().get("sha")
        
        encoded_content = base64.b64encode(content.encode()).decode()
        
        commit_message = message or f"Add/Update {path}"
        
        data = {
            "message": commit_message,
            "content": encoded_content,
            "branch": branch
        }
        
        if sha:
            data["sha"] = sha
        
        response = requests.put(url, headers=self.headers, json=data)
        
        if response.status_code in [200, 201]:
            return response.json()
        else:
            raise Exception(f"Failed to write file: {response.status_code} - {response.text}")

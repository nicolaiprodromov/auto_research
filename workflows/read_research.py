import os
import sys
import requests
import base64

def main():
    token = os.environ.get("PAT_TOKEN")
    owner = os.environ.get("GITHUB_OWNER")
    repo = os.environ.get("GITHUB_REPO")
    branch = os.environ.get("GITHUB_BRANCH", "master")
    file_path = "docs/index.md"
    subject = os.environ.get("RESEARCH_SUBJECT", "Marvin Pontiac")
    
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(url, headers=headers, params={"ref": branch})
        if response.status_code == 200:
            content = base64.b64decode(response.json()['content']).decode('utf-8')
            print(content)
        else:
            print(f"# Research on {subject}\n\n")
    except Exception as e:
        print(f"# Research on {subject}\n\n")

if __name__ == "__main__":
    main()

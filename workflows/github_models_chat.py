import sys
from clients.github_models_client import GitHubModelsClient
from clients.config import PAT_TOKEN, GITHUB_MODEL

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m workflows.github_models_chat <message>")
        sys.exit(1)
    
    message = " ".join(sys.argv[1:])
    
    try:
        client = GitHubModelsClient(token=PAT_TOKEN, model=GITHUB_MODEL)
        
        print("=" * 60)
        print("USER MESSAGE:")
        print(message)
        print("=" * 60)
        
        response = client.chat(message)
        
        print("AI RESPONSE:")
        print(response)
        print("=" * 60)
    
    except ValueError as e:
        print(f"Configuration error: {str(e)}")
        print("Please set PAT_TOKEN environment variable with your GitHub Personal Access Token")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

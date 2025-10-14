import sys
from clients.github_repo_client import GitHubRepoClient

def main():
    if len(sys.argv) < 3:
        print("Usage: python -m workflows.write_file <filename> <content>")
        sys.exit(1)
    
    filename = sys.argv[1]
    content = " ".join(sys.argv[2:])
    
    client = GitHubRepoClient()
    result = client.write_file(filename, content)
    
    print(f"File written successfully to GitHub: {filename}")
    print(f"Commit SHA: {result['commit']['sha']}")

if __name__ == "__main__":
    main()

import sys
from clients.tavily_client import TavilyClient

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m workflows.tavily_search <search_term>")
        sys.exit(1)
    
    search_term = " ".join(sys.argv[1:])
    
    client = TavilyClient()
    results = client.search(search_term)
    
    if results:
        print(f"\nSearch results for: {search_term}")
        print("-" * 50)
        print(results)
    else:
        print("No results found or an error occurred.")

if __name__ == "__main__":
    main()

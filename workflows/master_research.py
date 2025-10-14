import os
import time
import requests
from clients.github_models_client import GitHubModelsClient
from clients.tavily_client import TavilyClient
from clients.github_repo_client import GitHubRepoClient
from clients.config import PAT_TOKEN

DOCS_FILE_PATH = "docs/index.md"
RESEARCH_TOPIC = os.environ.get("RESEARCH_SUBJECT", "Marvin Pontiac")

def read_current_research(github_client):
    try:
        owner = os.environ.get("GITHUB_OWNER")
        repo = os.environ.get("GITHUB_REPO")
        branch = os.environ.get("GITHUB_BRANCH", "master")
        
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{DOCS_FILE_PATH}"
        headers = {
            "Authorization": f"Bearer {github_client.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.get(url, headers=headers, params={"ref": branch})
        if response.status_code == 200:
            import base64
            content = base64.b64decode(response.json()['content']).decode('utf-8')
            return content
        else:
            return f"# Research on {RESEARCH_TOPIC}\n\n"
    except Exception as e:
        print(f"File doesn't exist yet, starting fresh: {e}")
        return f"# Research on {RESEARCH_TOPIC}\n\n"

def write_research(github_client, content, message):
    result = github_client.write_file(DOCS_FILE_PATH, content, message)
    return result

def research_cycle():
    print(f"\n{'='*60}")
    print(f"Starting research cycle at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    github_client = GitHubRepoClient()
    model_client = GitHubModelsClient(token=PAT_TOKEN, model="gpt-4o-mini")
    tavily_client = TavilyClient()
    
    current_content = read_current_research(github_client)
    
    print("Step 1: Analyzing current research and determining search terms...")
    analysis_prompt = f"""You are a research assistant. Look at the current research about {RESEARCH_TOPIC}:

{current_content}

Based on what's already covered, suggest 3-5 specific search terms that would help us learn more unexplored aspects about {RESEARCH_TOPIC}. 
Return ONLY the search terms, one per line, without numbering or extra explanation."""
    
    search_terms_response = model_client.chat(analysis_prompt)
    if not search_terms_response:
        search_terms_response = f"{RESEARCH_TOPIC} biography\n{RESEARCH_TOPIC} music\n{RESEARCH_TOPIC} history"
    search_terms = [term.strip() for term in search_terms_response.strip().split('\n') if term.strip()]
    
    print(f"Generated search terms: {search_terms}\n")
    
    print("Step 2: Searching for information...")
    all_search_results = []
    for term in search_terms[:3]:
        print(f"  Searching: {term}")
        results = tavily_client.search(term, max_results=3)
        if results and 'results' in results:
            all_search_results.extend(results['results'])
    
    search_content = ""
    for idx, result in enumerate(all_search_results, 1):
        title = result.get('title', 'No title')
        content = result.get('content', '')
        url = result.get('url', '')
        search_content += f"\n[Source {idx}] {title}\n{content}\n{url}\n"
    
    print(f"Found {len(all_search_results)} results\n")
    
    print("Step 3: Generating new research content...")
    writing_prompt = f"""You are a research writer. Based on the search results below, write EXACTLY 10 informative sentences about {RESEARCH_TOPIC}. 

Current research context:
{current_content}

Search results:
{search_content}

Write 10 new sentences that add to our knowledge about {RESEARCH_TOPIC}. Make sure they are factual, well-written, and don't repeat what's already in the current research. Number each sentence from 1 to 10."""
    
    new_content = model_client.chat(writing_prompt)
    
    print("Step 4: Saving new research to repository...")
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_content = current_content + f"\n## Research Update - {timestamp}\n{new_content}\n"
    
    commit_message = f"Auto-research update: {timestamp}"
    write_research(github_client, updated_content, commit_message)
    
    print(f"Committed to repository: {commit_message}")
    print(f"\n{'='*60}")
    print("Research cycle completed successfully!")
    print(f"{'='*60}\n")

def main():
    print(f"Master Research Workflow - {RESEARCH_TOPIC}")
    print(f"Running single research cycle (scheduled by GitHub Actions every 10 minutes)\n")
    
    try:
        research_cycle()
    except Exception as e:
        print(f"Error in research cycle: {str(e)}")
        raise

if __name__ == "__main__":
    main()

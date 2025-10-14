import sys
import os
from clients.github_models_client import GitHubModelsClient
from clients.config import PAT_TOKEN

def main():
    if len(sys.argv) < 3:
        print("Usage: python -m workflows.synthesize_research <current_research> <search_results>")
        sys.exit(1)
    
    current_content = sys.argv[1]
    search_content = sys.argv[2]
    subject = os.environ.get("RESEARCH_SUBJECT", "Marvin Pontiac")
    
    model_client = GitHubModelsClient(token=PAT_TOKEN, model="gpt-4o-mini")
    
    writing_prompt = f"""You are a research writer. Based on the search results below, write EXACTLY 10 informative sentences about {subject}. 

Current research context:
{current_content}

Search results:
{search_content}

Write 10 new sentences that add to our knowledge about {subject}. Make sure they are factual, well-written, and don't repeat what's already in the current research. Number each sentence from 1 to 10."""
    
    new_content = model_client.chat(writing_prompt)
    print(new_content)

if __name__ == "__main__":
    main()

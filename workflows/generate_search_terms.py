import sys
import os
from clients.github_models_client import GitHubModelsClient
from clients.config import PAT_TOKEN

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m workflows.generate_search_terms <current_research_content>")
        sys.exit(1)
    
    current_content = sys.argv[1]
    subject = os.environ.get("RESEARCH_SUBJECT", "Marvin Pontiac")
    
    model_client = GitHubModelsClient(token=PAT_TOKEN, model="gpt-4o-mini")
    
    analysis_prompt = f"""You are a research assistant. Look at the current research about {subject}:

{current_content}

Based on what's already covered, suggest 3-5 specific search terms that would help us learn more unexplored aspects about {subject}. 
Return ONLY the search terms, one per line, without numbering or extra explanation."""
    
    search_terms_response = model_client.chat(analysis_prompt)
    if not search_terms_response:
        search_terms_response = f"{subject} biography\n{subject} music\n{subject} history"
    
    print(search_terms_response)

if __name__ == "__main__":
    main()

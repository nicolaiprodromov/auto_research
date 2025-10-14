import sys
import json
from src.github_models_client import GitHubModelsClient
from src.config import PAT_TOKEN, GITHUB_MODEL

def main():
    try:
        client = GitHubModelsClient(token=PAT_TOKEN, model=GITHUB_MODEL)
        
        print("GitHub Models Chat Workflow")
        print("=" * 50)
        print(f"Using model: {GITHUB_MODEL}")
        print("Type 'quit' or 'exit' to end the conversation")
        print("=" * 50)
        
        conversation_history = []
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("Ending conversation. Goodbye!")
                break
            
            if not user_input:
                continue
            
            conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            try:
                response = client.chat_with_history(conversation_history)
                
                conversation_history.append({
                    "role": "assistant",
                    "content": response
                })
                
                print(f"\nAssistant: {response}")
                
            except Exception as e:
                print(f"Error getting response: {str(e)}")
                conversation_history.pop()
        
        if conversation_history:
            save_choice = input("\nWould you like to save this conversation? (y/n): ").strip().lower()
            if save_choice == 'y':
                filename = input("Enter filename (without extension): ").strip()
                if filename:
                    with open(f"{filename}.json", 'w') as f:
                        json.dump(conversation_history, f, indent=2)
                    print(f"Conversation saved to {filename}.json")
    
    except ValueError as e:
        print(f"Configuration error: {str(e)}")
        print("Please set PAT_TOKEN environment variable with your GitHub Personal Access Token")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

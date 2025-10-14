import sys
import os
from datetime import datetime

def main():
    if len(sys.argv) < 3:
        print("Usage: python -m workflows.append_research <current_content_file> <new_content_file>")
        sys.exit(1)
    
    current_file = sys.argv[1]
    new_file = sys.argv[2]
    
    with open(current_file, 'r', encoding='utf-8') as f:
        current_content = f.read()
    
    with open(new_file, 'r', encoding='utf-8') as f:
        new_content = f.read()
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    updated_content = f"{current_content}\n## Research Update - {timestamp}\n{new_content}\n"
    
    print(updated_content)

if __name__ == "__main__":
    main()

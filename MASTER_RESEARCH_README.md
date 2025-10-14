# Master Research Workflow - Marvin Pontiac

This automated research workflow continuously gathers and compiles information about Marvin Pontiac.

## How It Works

1. **Every 10 minutes**, GitHub Actions triggers the workflow
2. The workflow uses the GitHub API to read the current `docs/index.md` file (creates it if missing)
3. Uses GPT-4o-mini to analyze what's already covered and generate 3-5 search terms for new research
4. Searches Tavily API with those terms to find relevant information
5. Uses GPT-4o-mini again to synthesize the search results into exactly 10 new sentences
6. Appends the new content with a timestamp to the existing research
7. Commits the updated content directly to the repository via GitHub API (using the same method as the `write_file.yml` workflow)
8. Repeats every 10 minutes

## Setup

1. Add the following secrets to your GitHub repository (Settings → Secrets and variables → Actions):
   - `PAT_TOKEN` - Your GitHub Personal Access Token (with repo write permissions)
   - `TAVILY_API_KEY` - Your Tavily API key
   - `TAVILY_API_URL` - Tavily API URL (default: https://api.tavily.com/search)

2. The workflow will start automatically every 10 minutes (researching "Marvin Pontiac" by default)

3. You can also trigger it manually via GitHub Actions and specify a custom subject to research

4. The workflow uses the GitHub API to commit changes (same as `write_file.yml`), so no local git operations are needed

## Customizing the Research Subject

### Via GitHub Actions UI:
1. Go to Actions tab in your repository
2. Select "Master Research" workflow
3. Click "Run workflow"
4. Enter your desired subject in the "Subject matter to research" field
5. Click "Run workflow"

### For Scheduled Runs:
The default subject is "Marvin Pontiac". To change the default, edit the `default` value in `.github/workflows/master_research.yml`

## Files

- `.github/workflows/master_research.yml` - GitHub Actions workflow that runs every 10 minutes
- `workflows/master_research.py` - Python script that orchestrates the research process
- `docs/index.md` - Output file where research is accumulated

## Manual Testing

To test locally:
```bash
python -m workflows.master_research
```

Make sure you have a `.env` file with:
```
PAT_TOKEN=your_github_token
TAVILY_API_KEY=your_tavily_key
TAVILY_API_URL=https://api.tavily.com/search
```

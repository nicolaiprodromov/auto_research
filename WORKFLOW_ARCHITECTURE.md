# Master Research Workflow - Architecture

## Workflow Graph Visualization

When you run this workflow in GitHub Actions, you'll see these steps as separate nodes in the workflow graph:

```
┌─────────────────────────┐
│   Checkout code         │
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│   Set up Python         │
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│  Install dependencies   │
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│ Read Current Research   │ ← Reads docs/index.md via GitHub API
└───────────┬─────────────┘
            │
┌───────────▼─────────────┐
│ Generate Search Terms   │ ← AI analyzes current research
└───────────┬─────────────┘
            │
      ┌─────┴─────┐
      │           │
┌─────▼──┐  ┌────▼───┐  ┌─────▼──┐
│Search 1│  │Search 2│  │Search 3│ ← Parallel Tavily searches
└─────┬──┘  └────┬───┘  └─────┬──┘
      │           │            │
      └───────┬───┴────────────┘
              │
┌─────────────▼─────────────┐
│   Synthesize Research     │ ← AI writes 10 new sentences
└─────────────┬─────────────┘
              │
┌─────────────▼─────────────┐
│ Write Research to Repo    │ ← Commits to docs/index.md
└───────────────────────────┘
```

## Individual Steps

### 1. **Read Current Research**
- Script: `workflows/read_research.py`
- Uses GitHub API to read `docs/index.md`
- Outputs: current research content

### 2. **Generate Search Terms**
- Script: `workflows/generate_search_terms.py`
- Uses GPT-4o-mini to analyze current research
- Outputs: 3-5 search terms

### 3. **Search Term 1/2/3**
- Script: `workflows/tavily_search.py` (existing)
- Runs Tavily searches in parallel
- Each outputs their search results

### 4. **Synthesize Research**
- Script: `workflows/synthesize_research.py`
- Uses GPT-4o-mini to write 10 new sentences
- Takes current research + all search results
- Outputs: new research content

### 5. **Write Research to Repository**
- Script: `workflows/write_file.py` (existing)
- Commits updated content to `docs/index.md`
- Uses GitHub API

## Benefits

✅ **Visual Workflow Graph**: Each step shows as a separate node in GitHub Actions UI
✅ **Granular Monitoring**: See which step succeeds/fails
✅ **Reusable Components**: Each workflow script can be used independently
✅ **Parallel Execution**: Search steps can run in parallel (if configured)
✅ **Clear Data Flow**: Outputs from one step feed into the next

## Running Every 10 Minutes

The workflow runs automatically via `cron: '*/10 * * * *'` schedule.
You can also trigger manually with a custom subject.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an educational tutorial repository that teaches AI-assisted development workflow. It does not contain application code by default—students fork this repo and build a Streamlit sales dashboard as part of the tutorial.

The tutorial teaches a complete workflow: PRD → spec-kit → Jira → Code → Commit → Push → Deploy

## Key Files and Directories

- `prd/ecommerce-analytics.md` - Product requirements document for the dashboard
- `data/sales-data.csv` - Sample e-commerce transaction data (~1000 records)
- `docs/` - Tutorial documentation (numbered in reading order)

## Expected Student Output

When students complete the tutorial, their fork will contain:
- `app.py` - Streamlit dashboard application
- `requirements.txt` - Python dependencies (streamlit, pandas, plotly)
- `.specify/` - spec-kit artifacts (constitution, spec, plan, tasks)
- `specs/` - Generated specifications from spec-kit

## Tech Stack for Dashboard

- **Python 3.11+** with virtual environment
- **Streamlit** for the web dashboard
- **Pandas** for data processing
- **Plotly** for interactive charts

## Workflow Commands

The tutorial uses spec-kit slash commands (requires `specify init . --ai claude` first):
- `/speckit.constitution` - Create project principles
- `/speckit.specify` - Generate specification from PRD
- `/speckit.plan` - Create implementation plan
- `/speckit.tasks` - Generate task breakdown
- `/speckit.implement` - Implement a task

## Jira Integration

The tutorial uses Atlassian MCP server for Jira integration:
```bash
claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
```

Project key is `ECOM`. Commits should reference Jira issues (e.g., `ECOM-1: add sales dashboard`).

## Running the Dashboard

After implementation, run locally with:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
streamlit run app.py
```

Dashboard deploys to Streamlit Community Cloud from the `main` branch.

# Glossary

A reference guide to key terms used in this tutorial.

---

## Git and Version Control

| Term | Definition |
|------|------------|
| **Branch** | A separate copy of your code where you can make changes without affecting the main version. |
| **Clone** | Creating a local copy of a remote repository on your computer. |
| **Commit** | A snapshot of your project at a specific moment, like a "save point." |
| **Commit Hash** | A unique ID for each commit (like `abc1234`), used to reference specific snapshots of code. |
| **Feature Branch** | A branch created for developing a specific feature, separate from main (e.g., `001-sales-dashboard`). |
| **Fork** | Your personal copy of someone else's repository on GitHub. |
| **Git** | Version control software that tracks changes to files over time. |
| **GitHub** | A website that hosts Git repositories in the cloud and enables collaboration. |
| **Merge** | Combining changes from one branch into another (e.g., feature branch into main). |
| **Pull** | Downloading changes from a remote repository to your local copy. |
| **Push** | Uploading your local commits to a remote repository. |
| **Repository (Repo)** | A project folder tracked by Git, containing files and complete history. |
| **Staging Area** | A holding area for changes you want to include in your next commit. |

---

## Development Tools

| Term | Definition |
|------|------------|
| **Claude Code** | Anthropic's AI assistant that runs in your terminal and helps with coding tasks. |
| **CLI** | Command Line Interface — a text-based way to interact with your computer by typing commands. |
| **Cursor** | An AI-powered code editor built on VS Code with integrated AI features. |
| **IDE** | Integrated Development Environment — software for writing and managing code (e.g., Cursor, VS Code). |
| **MCP** | Model Context Protocol — a system that allows Claude Code to connect to external services like Jira. |
| **Terminal** | A text-based interface for running commands on your computer. Also called "command line" or "shell." |

---

## Project Management

| Term | Definition |
|------|------------|
| **Epic** | A large body of work in Jira that can be broken down into smaller tasks or stories. |
| **Issue** | A trackable work item in Jira (can be a Story, Task, or Bug). |
| **Jira** | A project management tool used by teams to track tasks and progress. |
| **Sprint** | A fixed time period (usually 1-2 weeks) during which specific work is completed. |
| **Story** | A user-facing feature described from the user's perspective ("As a user, I want..."). |
| **Task** | A technical work item that needs to be completed. |
| **Traceability** | The ability to connect code changes back to requirements and track why changes were made. |

---

## Spec-Driven Development

| Term | Definition |
|------|------------|
| **Constitution** | In spec-kit, a document defining the project's standards and conventions. |
| **PRD** | Product Requirements Document — a written specification describing what to build and why. |
| **Specification** | A detailed description of requirements and expected behavior for a feature. |
| **spec-kit** | GitHub's toolkit for spec-driven development that helps convert requirements into code. |

---

## Python and Data

| Term | Definition |
|------|------------|
| **CSV** | Comma-Separated Values — a simple file format for storing tabular data (rows and columns). |
| **Dashboard** | A visual display showing multiple charts and metrics on one screen. |
| **DataFrame** | A table-like data structure in Pandas used for data manipulation. |
| **KPI** | Key Performance Indicator — a metric showing important business data at a glance. |
| **Pandas** | A Python library for data manipulation and analysis. |
| **pip** | Python's package installer for adding libraries to your project. |
| **Plotly** | A Python library for creating interactive charts and visualizations. |
| **Streamlit** | A Python library that turns code into interactive web applications without HTML/CSS. |
| **uv** | A fast Python package installer and virtual environment manager. |
| **Virtual Environment (venv)** | An isolated Python environment that keeps project dependencies separate. |

---

## File and System Terms

| Term | Definition |
|------|------------|
| **.gitignore** | A file telling Git which files or folders to ignore and not track. |
| **Absolute Path** | A complete path from the root of your file system (e.g., `/Users/alex/projects`). |
| **Directory** | Another name for a folder. |
| **Home Directory** | Your user folder (e.g., `/Users/yourname` on macOS, `C:\Users\yourname` on Windows). |
| **Path** | The location of a file or folder in your file system. |
| **Relative Path** | A path starting from your current location (e.g., `../Documents`). |
| **Root** | The top-level directory of a file system (`/` on macOS/Linux, `C:\` on Windows). |

---

## Workflow Terms

| Term | Definition |
|------|------------|
| **Deployment** | Releasing software to a server where users can access it. |
| **Local** | On your computer (as opposed to "remote" which is on a server). |
| **Remote** | On a server (e.g., GitHub), not on your local computer. |
| **Streamlit Community Cloud** | A free hosting service for Streamlit apps, making dashboards publicly accessible. |

---

## Quick Reference by Document

### Session 1: Setup
- Claude Code, Cursor, Git, GitHub, Jira, CLI, Terminal, Fork, Clone, MCP

### Session 2: Workflow
- Branch, Feature Branch, Merge, Commit, Commit Hash, Push, spec-kit, PRD, KPI, Streamlit, Virtual Environment, Deployment, Streamlit Community Cloud

### Troubleshooting
- Path, .gitignore, pip, Virtual Environment, Staging Area

---

## Need More Help?

If you encounter a term not listed here:
1. Ask Claude Code: "What does [term] mean?"
2. Check the [FAQ](07-faq.md) for common questions
3. Search online for the specific term in context

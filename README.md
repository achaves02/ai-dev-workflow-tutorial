# AI-Assisted Development Workflow Tutorial

A hands-on tutorial for establishing a complete, end-to-end, AI-assisted software development workflow using Cursor, Claude Code, GitHub, and Jira.

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│   PRD   │ →  │ spec-kit │ →  │  Jira   │ →  │ Branch │
└─────────┘    └──────────┘    └─────────┘    └────────┘
                                                  ↓
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│  Merge  │ ←  │    PR    │ ←  │ Commit  │ ←  │  Code  │
└─────────┘    └──────────┘    └─────────┘    └────────┘
```

## Why This Matters

### The Industry Has Changed

Software development in 2026 looks fundamentally different than it did just two years ago. AI coding assistants have moved from novelty to necessity. Companies expect new hires to work effectively with AI tools, and those who can are dramatically more productive.

**This is not about replacing developers — it's about amplifying them.**

Developers who use AI assistants effectively:
- Ship features faster while maintaining quality
- Spend less time on boilerplate and more on creative problem-solving
- Debug issues more efficiently with AI-powered analysis
- Learn new technologies faster with AI as a teaching partner

### Professional Workflows Create Professional Results

Every successful software team follows a structured workflow. This isn't bureaucracy — it's how teams coordinate, maintain quality, and move quickly without breaking things.

```
┌─────────────────────────────────────────────────────────────┐
│                    Why Workflows Matter                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Without Workflow:              With Workflow:              │
│  ─────────────────              ───────────────             │
│  • "Who changed this?"          • Full audit trail          │
│  • "Is this the latest?"        • Single source of truth    │
│  • "What broke it?"             • Easy to trace and fix     │
│  • "What are we building?"      • Clear requirements        │
│  • Chaos at scale               • Scales to any team size   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

The workflow you learn in this tutorial is used at companies from startups to Fortune 500:
- **GitHub** for code (used by 100M+ developers)
- **Jira** for task tracking (used by 65K+ companies)
- **Pull requests** for code review (industry standard)
- **Branch-based development** (universal practice)

### Your Competitive Advantage

By completing this tutorial, you will have skills that many working developers are still acquiring:

1. **AI-Assisted Development**: Using Claude Code as a thinking and implementation partner
2. **Spec-Driven Development**: Turning requirements into code systematically
3. **Full Traceability**: Connecting every line of code to a business requirement
4. **Industry Tooling**: Hands-on experience with the tools companies actually use

These are not "student skills" — these are professional skills that will set you apart in interviews and on the job.

---

## What You Will Learn

By the end of this tutorial, you will be able to:

- Move from a tracked task to merged production-ready code
- Use Claude Code as a thinking and implementation assistant
- Maintain full traceability: Jira issue → branch → commit → PR → merge
- Apply spec-driven development using GitHub's spec-kit

## Tutorial Structure

This tutorial is designed for two 100-minute sessions:

### Session 1: Setup & Foundation

| Document | Description |
|----------|-------------|
| [Overview](docs/00-overview.md) | Tutorial objectives and what you'll build |
| [Session 1: Setup](docs/01-session-1-setup.md) | Account creation and tool installation |
| [Terminal Basics](docs/02-terminal-basics.md) | Essential command-line skills |
| [Git Concepts](docs/03-git-concepts.md) | Version control fundamentals |

### Session 2: Spec-Driven Workflow

| Document | Description |
|----------|-------------|
| [Session 2: Workflow](docs/04-session-2-workflow.md) | Complete development workflow |

### Reference Materials

| Document | Description |
|----------|-------------|
| [Troubleshooting](docs/05-troubleshooting.md) | Common issues and solutions |
| [Next Steps](docs/06-next-steps.md) | Applying this workflow to your capstone |
| [FAQ](docs/07-faq.md) | Frequently asked questions |

## Project Materials

| Resource | Description |
|----------|-------------|
| [E-Commerce PRD](prd/ecommerce-analytics.md) | Product requirements document |
| [Sales Data](data/sales-data.csv) | Sample dataset for the dashboard |

## Prerequisites

No prior experience with Git, Jira, or AI coding tools is required. You should have:

- A computer running macOS or Windows
- Basic Python knowledge
- Familiarity with VS Code (Cursor is VS Code-based)

## Tools You Will Use

| Tool | Purpose | Industry Context |
|------|---------|------------------|
| **GitHub** | Version control and code hosting | Used by 100M+ developers worldwide |
| **Jira** | Project and task management | Used by 65,000+ companies |
| **Cursor** | AI-powered code editor | Leading AI-native IDE |
| **Claude Code** | AI coding assistant (CLI) | State-of-the-art AI assistant |
| **spec-kit** | Spec-driven development toolkit | Modern requirements-to-code workflow |

## Quick Start

1. Fork this repository to your GitHub account
2. Follow [Session 1: Setup](docs/01-session-1-setup.md) to configure your environment
3. Continue with [Session 2: Workflow](docs/04-session-2-workflow.md) to build the dashboard

## Naming Conventions

This tutorial uses consistent naming conventions (kebab-case):

| Item | Convention | Example |
|------|------------|---------|
| Jira Project Key | UPPERCASE | `ECOM` |
| Jira Issue | KEY-NUMBER | `ECOM-1` |
| Branch | feature/KEY-NUMBER-description | `feature/ECOM-1-add-sales-dashboard` |
| Commit | KEY-NUMBER: description | `ECOM-1: add sales dashboard` |

## Getting Help

- **During class**: Ask your instructor
- **Outside class**: Post in the Teams channel
- **Technical issues**: Ask Claude Code for help — it can diagnose and fix most problems

## License

This tutorial is provided for educational purposes.

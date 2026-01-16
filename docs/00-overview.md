# Tutorial Overview

## Why You Are Here

### The Most In-Demand Skill Set of 2026

Building with technology in 2026 looks fundamentally different than it did just two years ago. AI assistants have moved from experimental to essential. Companies are actively seeking professionals who can work effectively with AI tools to build solutions — and struggling to find them.

**This is not about becoming a software engineer — it's about being able to build solutions with technology and data.**

Whether you become a business analyst, data scientist, product manager, consultant, or entrepreneur, you will need to build dashboards, automate workflows, create prototypes, and collaborate with technical teams. AI-assisted building makes all of this dramatically more accessible.

**You are learning this skill now, at the beginning of your career.** This puts you ahead of many experienced professionals who are still adapting.

Consider what AI-assisted building enables:

| Traditional Approach | AI-Assisted Approach |
|---------------------|---------------------|
| Google for solutions, copy from Stack Overflow | Ask Claude Code to explain and implement |
| Hours debugging with print statements | AI analyzes errors and suggests fixes |
| Write boilerplate code manually | AI generates scaffolding, you focus on business logic |
| Learn frameworks by reading documentation | AI teaches you as you build |
| Work alone, limited by your knowledge | AI as a knowledgeable partner |

### The Workflow You Will Master

Every technology company — from startups to Google, Meta, and Microsoft — uses a variation of this workflow:

```
┌─────────────────────────────────────────────────────────────┐
│                  AI-Assisted Building Workflow               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Requirements      → What are we building and why?       │
│  2. Task Tracking     → Break work into trackable pieces    │
│  3. Version Control   → Manage code changes safely          │
│  4. AI-Assisted Code  → Build with Claude Code as partner   │
│  5. Deploy & Share    → Make your work accessible           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

In interviews, you will be asked about Git and collaborative workflows. This tutorial gives you hands-on experience — not just theoretical knowledge.

> **Note:** Full branching and pull request workflows are introduced in capstone projects. This tutorial focuses on the core skills: building with AI assistance, version control basics, and deploying your work.

### What Makes This Tutorial Different

This is not a toy exercise. You are:

- Using **real tools** that companies pay for (GitHub, Jira, Claude Pro)
- Following **real workflows** used by professional teams
- Building a **real deliverable** (a working dashboard)
- Learning **real skills** that transfer directly to your capstone and career

These are not "student skills" — these are professional skills that set you apart in interviews and on the job, regardless of your specific role.

---

## Objective

This tutorial establishes a complete, end-to-end, AI-assisted workflow for building technology solutions. By the end, you will be able to move from a tracked task to a deployed, shareable solution using Cursor, Claude Code, GitHub, and Jira with explicit integrations and traceability.

## What You Will Build

You will create a **Streamlit sales dashboard** for a fictional e-commerce retailer. The dashboard will include:

- **2 KPI scorecards** at the top (Total Sales, Number of Orders)
- **1 line chart** showing sales trend over time
- **2 bar charts** showing sales breakdown by category and region

```
┌─────────────────────────────────────────────────────────────┐
│                E-Commerce Sales Dashboard                    │
├────────────────────────────┬────────────────────────────────┤
│       Total Sales          │       Total Orders             │
│       $1,234,567           │       8,432                    │
├────────────────────────────┴────────────────────────────────┤
│                   Sales Trend (Line Chart)                   │
│    $                                                         │
│    │      ╱╲        ╱╲                                       │
│    │     ╱  ╲      ╱  ╲      ╱                              │
│    │    ╱    ╲    ╱    ╲    ╱                               │
│    │   ╱      ╲  ╱      ╲  ╱                                │
│    │  ╱        ╲╱        ╲╱                                 │
│    └──────────────────────────────────────────── time       │
├────────────────────────────┬────────────────────────────────┤
│    Sales by Category       │    Sales by Region             │
│    (Bar Chart)             │    (Bar Chart)                 │
└────────────────────────────┴────────────────────────────────┘
```

The dashboard itself is just the vehicle. The real learning is the **process** you follow to build it.

## The Workflow You Will Learn

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Your Development Workflow                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌─────────┐     ┌──────────┐     ┌─────────┐     ┌────────┐          │
│   │   PRD   │ ──► │ spec-kit │ ──► │  Jira   │ ──► │  Code  │          │
│   │(written)│     │(Claude)  │     │(tracking)│     │(Claude)│          │
│   └─────────┘     └──────────┘     └─────────┘     └────────┘          │
│                                                          │              │
│                                                          ▼              │
│   ┌─────────┐     ┌──────────┐     ┌─────────┐     ┌────────┐          │
│   │  Live!  │ ◄── │  Deploy  │ ◄── │  Push   │ ◄── │ Commit │          │
│   │(public) │     │(Streamlit)│     │(GitHub) │     │(Git)   │          │
│   └─────────┘     └──────────┘     └─────────┘     └────────┘          │
│                                                                         │
│   Legend: (tool) = primary tool used for this step                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Step-by-Step Flow

1. **PRD (Product Requirements Document)**: Start with a written specification of what to build
2. **spec-kit**: Use AI-assisted tools to refine requirements into a technical plan
3. **Jira**: Create trackable tasks from the plan
4. **Code**: Build the feature using Claude Code assistance
5. **Commit**: Save your changes with a meaningful message
6. **Push**: Upload your code to GitHub
7. **Deploy**: Make your dashboard publicly accessible on Streamlit Community Cloud

## Key Concepts

### Traceability

Every piece of code can be traced back to a requirement:

```
Jira Issue: ECOM-1 "Create sales dashboard"
     ↓
Commit: "ECOM-1: add sales dashboard with KPIs and charts"
     ↓
Push: Code is now on GitHub, linked to Jira
     ↓
Deploy: Dashboard is live and shareable
```

**Why this matters in your career:**
- When something breaks, you can find out exactly when and why
- Project managers can track progress by looking at linked commits
- New team members can understand why code exists
- Anyone can verify what was built and when

### Spec-Driven Development

Instead of jumping straight to code, you:

1. **Specify** what you want to build (clear requirements)
2. **Plan** how you will build it (technical approach)
3. **Break down** the work into tasks (manageable pieces)
4. **Implement** with AI assistance (guided coding)

This approach reduces wasted effort and produces better results.

**Common mistake:** Skipping specification wastes time building the wrong thing. AI amplifies this — you can build the wrong thing very fast. Spec-driven development ensures you build the right thing.

### AI as a Partner

Claude Code is not just a code generator. It helps you:

- Understand requirements and ask clarifying questions
- Plan your approach before writing code
- Write code with explanations
- Debug issues when things go wrong
- Learn new concepts as you work

**How to think about AI assistance:**

```
┌─────────────────────────────────────────────────────────────┐
│                   AI Partnership Model                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  YOU provide:                  AI provides:                 │
│  ────────────                  ────────────                 │
│  • Direction and goals         • Implementation speed       │
│  • Domain knowledge            • Technical knowledge        │
│  • Quality judgment            • Pattern recognition        │
│  • Final decisions             • Options and explanations   │
│  • Accountability              • Tireless assistance        │
│                                                             │
│  TOGETHER you achieve what neither could alone.             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Session Structure

### Session 1: Setup & Foundation (100 minutes)

By the end of Session 1, you will have:

- GitHub account with forked tutorial repository
- Atlassian account with Jira project
- Cursor installed with Claude Code configured
- Git installed and configured
- Python 3.11+ with uv and spec-kit installed

### Session 2: Spec-Driven Workflow (100 minutes)

By the end of Session 2, you will have:

- Atlassian MCP server connected to Claude Code
- Spec-kit constitution, specification, and plan created
- Jira issue created from spec-kit tasks
- Streamlit dashboard built and committed
- Code pushed to GitHub
- Dashboard deployed to Streamlit Community Cloud

## Completion Checklist

Use this checklist to verify your tutorial is complete:

### Session 1 Checkpoints
- [ ] GitHub account created
- [ ] Atlassian/Jira account created
- [ ] Claude Pro subscription active
- [ ] Cursor installed
- [ ] Claude Code working in Cursor terminal
- [ ] Git installed and configured
- [ ] Python 3.11+ installed
- [ ] uv installed
- [ ] spec-kit installed
- [ ] Tutorial repo forked and cloned
- [ ] Jira project created (ECOM)

### Session 2 Checkpoints
- [ ] Atlassian MCP server connected
- [ ] spec-kit constitution created
- [ ] spec-kit specification created
- [ ] spec-kit plan created
- [ ] spec-kit tasks generated
- [ ] Jira issues created from tasks (ECOM-1, ECOM-2, etc.)
- [ ] Streamlit dashboard built
- [ ] Changes committed with Jira keys
- [ ] Jira issues updated with evidence (commit hash, branch, GitHub link)
- [ ] Feature branch merged to main
- [ ] Code pushed to GitHub
- [ ] Dashboard deployed to Streamlit Community Cloud

## After This Tutorial

The skills you learn here directly apply to:

1. **Your Capstone Project**: Use this exact workflow with your team
2. **Internships**: You'll be productive from day one
3. **Any Role**: Business analysts, data scientists, product managers, consultants — all benefit from knowing how to build with AI and collaborate using professional tools
4. **Personal Projects**: Build dashboards, automate workflows, and create solutions faster on your own

## Next Steps

Ready to begin? Start with [Session 1: Setup](01-session-1-setup.md).

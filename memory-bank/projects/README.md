---
owner: [Project Owner]
last_updated: YYYY-MM-DD
size: 🟢
status: template
sources_of_truth: [projects/README.md]
related_files: [activeContext.md, ceo-dashboard.md]
---

# 📁 Projects Directory

**Purpose:** Centralized hub for organizing business projects with detailed context
**Navigation:** Each project has its own directory with complete documentation
**For Quick Status:** See [ceo-dashboard.md](../ceo-dashboard.md) for 5-second scan

## 📊 Project Status Overview

**Active Projects:** [Number]
**Pipeline Projects:** [Number]
**Archived Projects:** [Number]

---

## 📁 Project Directory Structure

Projects use one of two structures depending on complexity:

### Standard Structure (Most Projects)

For client delivery, product development, and operational projects:

```
projects/[project-name]/
├── README.md           # Navigation hub and quick reference
├── context.md          # Detailed project context
├── CHANGELOG.md        # Weekly learning record (wins, pivots, next steps)
├── decisions.md        # Key decisions and rationale
├── progress.md         # Implementation progress tracking
└── [additional docs]   # Project-specific documentation
```

**When to Use:**
- ✅ Client delivery projects (consulting, implementation)
- ✅ Product development (features, integrations)
- ✅ Operational improvements (internal tooling)
- ✅ Single-phase execution (clear start and end)
- ✅ Documentation <20K words

**Example Use Cases:**
- Client transformation projects
- SaaS product features
- Internal automation tools
- VA hiring and delegation systems

**Template Location:** `example-templates/standard-project/`

---

### Enhanced Structure (Complex Multi-Phase Projects)

For projects with extensive strategy, multiple expert analyses, or multi-year execution phases:

```
projects/[project-name]/
├── README.md           # Executive summary and navigation hub
├── CHANGELOG.md        # Weekly progress, decisions, insights, success metrics
├── strategy/           # Main strategy documents (PLANNING - what to do)
│   ├── [main-strategy].md            # Comprehensive acquisition/execution strategy
│   ├── [implementation-plans].md     # Detailed implementation blueprints
│   └── [financial-models].md         # Financial projections and scenarios
├── analysis/           # Validation documents (PROOF - why it works)
│   ├── [expert-analysis].md          # Expert board reviews and validations
│   ├── [ai-comparisons].md           # AI-generated second opinions
│   └── [due-diligence].md            # Research and validation reports
└── coordination/       # Tracking documents (EXECUTION - how to track)
    ├── [issue-templates].md          # GitHub issue templates
    ├── [meeting-agendas].md          # Partnership/team coordination
    └── [milestone-tracking].md       # Phase-by-phase execution tracking
```

**When to Use Enhanced Structure:**
- ✅ Projects with 20K+ words of strategy documentation
- ✅ Multiple expert analyses or AI validation needed (board reviews, AI comparisons)
- ✅ Multi-phase execution spanning 2+ years (Phase 1 → Phase 2 → Phase 3)
- ✅ Partnership or joint venture structures requiring coordination
- ✅ Complex deal flow with multiple sourcing strategies
- ✅ Strategic initiatives requiring extensive validation
- ❌ Single-phase client delivery projects (use Standard Structure)
- ❌ Operational improvements without strategic planning phase (use Standard Structure)

**Example Use Cases:**
- Private equity acquisition strategies
- Multi-year partnership ventures
- Complex M&A initiatives
- Strategic business pivots with extensive planning

**Template Location:** `example-templates/enhanced-project/`

---

### File Placement Guidelines

#### **strategy/** = Planning documents (what to do)
- Acquisition strategies, deal sourcing playbooks, financial models
- Business plans, go-to-market strategies, competitive analysis
- Partnership agreements, equity structures, operating rhythms
- **File Size:** Typically 🔴 (>600 lines) for comprehensive strategies
- **Read when:** Planning phases, strategic pivots, partner alignment meetings
- **Examples:** 3-phase acquisition strategy, deal sourcing playbook, 5-year financial models

#### **analysis/** = Validation documents (why it works)
- Expert board analysis, AI comparisons (Claude vs Gemini, etc.)
- Due diligence reports, market research, competitive assessments
- Risk analysis, feasibility studies, validation reports
- **File Size:** Typically 🟢 (<400 lines) for focused analyses
- **Read when:** Decision validation, risk assessment, second opinions needed
- **Examples:** Expert board consensus, AI validation comparison, due diligence summary

#### **coordination/** = Tracking documents (how to execute)
- GitHub issue templates, meeting agendas, milestone checklists
- Partnership coordination materials, weekly sync formats
- Phase-by-phase execution tracking, sprint planning
- **File Size:** Typically 🟢 (<400 lines) for operational docs
- **Read when:** Executing sprints, coordinating multi-party work, tracking milestones
- **Examples:** 30-day partnership formation sprint, GitHub issue templates, weekly meeting agendas

---

### CHANGELOG.md (Weekly Learning Record)

**Purpose:** Concise weekly record of learnings, wins, and strategic pivots for future planning and historical reference.

**Format:**
- Week header with date range
- Key Learning (1-2 sentences)
- Strategic Pivot (if applicable, From/To format)
- Wins (bullet list, 3-5 max)
- Next Steps (action items with owners)
- Status Change (Old → New, if applicable)
- Metrics (optional, only if relevant)

**When to Update:** See [memory-bank-rules.md § Changelog Update Decision Framework](../guides/memory-bank-rules.md)
- Weekly meetings completed
- Strategic pivots occur
- Key learnings discovered
- Major milestones achieved
- Status changes happen
- Significant wins accomplished

**Rule of Thumb:** "Would you want to remember this when planning next quarter or reviewing what happened?" → Yes = Update

---

## 🎯 Using Project Templates

### Option 1: Copy Standard Project Template

```bash
# From Template repository
cp -r memory-bank/projects/example-templates/standard-project/ memory-bank/projects/[your-project-name]/

# Customize
cd memory-bank/projects/[your-project-name]/
# Edit README.md, context.md, CHANGELOG.md with your project details
```

### Option 2: Copy Enhanced Project Template

```bash
# From Template repository
cp -r memory-bank/projects/example-templates/enhanced-project/ memory-bank/projects/[your-project-name]/

# Add your strategy documents
cd memory-bank/projects/[your-project-name]/strategy/
# Add main-strategy.md, implementation-plans.md, etc.

# Add your analysis documents
cd ../analysis/
# Add expert-analysis.md, ai-comparisons.md, etc.

# Add your coordination documents
cd ../coordination/
# Add issue-templates.md, meeting-agendas.md, etc.
```

---

## 📋 Project Lifecycle

### Active
Projects receiving active attention and resources. Full context maintained in project directory.

### Pipeline
Opportunities being nurtured, leads qualified, proposals in development. Lightweight tracking.

### Archived
Completed projects or closed opportunities. Moved to archive with completion summary.
**Archive Location:** `memory-bank/archive/projects/[year]/[project-name]/`

---

## 🎯 Usage Guidelines

### For Daily Operations
- Use [ceo-dashboard.md](../ceo-dashboard.md) for 5-second project status
- Reference this README for complete project list
- Dive into specific project directory for detailed context

### For Strategic Planning
- Use [activeContext.md](../activeContext.md) for strategic themes and weekly priorities
- Reference project directories for detailed status and history
- Update both ceo-dashboard.md and project context.md when status changes

### For Project Updates
1. Update project's `context.md` or `README.md` with detailed changes
2. Update project's `progress.md` or `CHANGELOG.md` with milestones
3. Update [ceo-dashboard.md](../ceo-dashboard.md) with next actions
4. Reference project changes in [activeContext.md](../activeContext.md) strategic summary

---

## 🔄 Decision Tree: Which Structure to Use?

```
Is this project documentation >20K words?
├─ YES → Consider Enhanced Structure
│   ├─ Multiple expert analyses needed? → Enhanced
│   ├─ Multi-phase execution (2+ years)? → Enhanced
│   ├─ Partnership/joint venture? → Enhanced
│   └─ Single client delivery? → Standard
│
└─ NO → Standard Structure
    ├─ Client delivery project → Standard
    ├─ Product feature → Standard
    ├─ Operational improvement → Standard
    └─ Internal tooling → Standard
```

---

**Navigation:** [Back to activeContext.md](../activeContext.md) | [CEO Dashboard](../ceo-dashboard.md) | [Start Here](../startHere.md)

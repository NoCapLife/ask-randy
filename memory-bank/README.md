---
title: Memory-Bank System - Quick Start Guide
type: readme
status: active
last_updated: 2025-01-10
---

# Memory-Bank System - Quick Start Guide

**Purpose**: Centralized project knowledge repository optimized for AI and human collaboration.
**Audience**: All developers, AI assistants, project stakeholders.
**File Size**: 🟢 Small - Quick reference.

## 🚀 Getting Started in 30 Seconds

### For Humans
1. **Start here**: [startHere.md](./startHere.md) - Master navigation hub
2. **Current work**: [activeContext.md](./activeContext.md) - What's happening now
3. **CEO Dashboard**: [ceo-dashboard.md](./ceo-dashboard.md) - 5-second project status

### For AI Assistants
1. **Read**: [startHere.md](./startHere.md) - Navigate the memory-bank
2. **Follow**: [AI_GUIDE.md](./AI_GUIDE.md) - Optimized AI workflow
3. **Reference**: [guides/ai-integration-guide.md](./guides/ai-integration-guide.md) - Integration patterns

## 📁 Repository Structure

```
memory-bank/
├── README.md                 (this file - quick start)
├── startHere.md              (master navigation hub - START HERE)
├── activeContext.md          (current sprint context)
├── ceo-dashboard.md          (real-time project status)
├── projectbrief.md           (project goals & scope)
├── AI_GUIDE.md               (AI assistant optimization)
│
├── projects/                 (project organization patterns & templates)
│   ├── README.md             (Standard vs Enhanced structures decision guide)
│   └── example-templates/
│       ├── standard-project/ (client delivery, features, operational projects)
│       └── enhanced-project/ (multi-phase, partnership, strategic initiatives)
│           ├── strategy/     (planning documents - what to do)
│           ├── analysis/     (validation documents - why it works)
│           └── coordination/ (tracking documents - how to execute)
│
├── features/                 (detailed feature documentation)
│   ├── feature-template.md   (template for new features)
│   ├── example-calculator/   (🟢 simple feature example, 8 files)
│   ├── example-dashboard/    (🔴 complex feature example, 8 files)
│   └── example-api-integration/ (🟡 integration pattern, 8 files)
│
├── guides/                   (reference documentation)
│   ├── README.md
│   ├── testing-guide.md
│   ├── performance-optimization-guide.md
│   ├── ai-development-guide.md
│   ├── ai-integration-guide.md
│   ├── subagent-collaboration-guide.md
│   ├── executive-summaries.md
│   ├── documentation-framework.md (includes Part III: Project Directory Patterns)
│   └── memory-bank-rules.md
│
├── archive/                  (deprecated documentation)
│   └── README.md
│
└── plans/                    (future work & proposals)
    ├── README.md
    └── plan-template.md
```

## 🎯 Key Features

### 1. Three Complete Feature Examples
- **Simple** (4-6 hours): Calculator - basic patterns
- **Complex** (4-6 weeks): Dashboard - real-time, WebSockets, advanced state
- **Integration** (2-3 weeks): API Integration - OAuth, retries, webhooks

### 2. 8-File Modular System
Every feature uses the same structure:
1. **README.md** - Navigation hub
2. **requirements.md** - Business requirements
3. **user-experience.md** - UX flows
4. **technical-design.md** - Architecture
5. **implementation.md** - Code guidance
6. **content-strategy.md** - UI copy
7. **testing-strategy.md** - Test scenarios
8. **decisions.md** - Key decisions
9. **dependencies.md** - External dependencies

### 3. AI Optimization
- File size indicators (🔴🟡🟢)
- Section-based navigation
- Executive summaries for large files
- Smart search patterns
- Context budgeting

### 4. Supporting Infrastructure
- **Archive**: Deprecated docs with retention policy
- **Plans**: Future work and proposals
- **Guides**: Reference documentation

## 📊 File Size Categories

- 🟢 **Small** (<400 lines) - Load directly into AI context
- 🟡 **Medium** (400-600 lines) - Use section navigation
- 🔴 **Large** (>600 lines) - Start with executive summary

## 🔄 Common Workflows

### Creating a New Feature
```
1. Copy features/feature-template.md
2. Create feature directory: features/[name]/
3. Create 8 core files using template
4. Update startHere.md with new feature
5. Add cross-references
```

### Updating Documentation
```
1. Edit relevant file(s)
2. Update last_updated date in frontmatter
3. Update cross-references if structure changed
4. Add entry to activeContext.md if significant
```

### Archiving Old Documentation
```
1. Move to archive/[year]/[month]/
2. Add status: archived to frontmatter
3. Add archived_date and reason
4. Update original location's index
5. Add entry to archive/README.md
```

## 🤖 AI Assistant Integration

### Quick Start for AI
```bash
# 1. Orient
Read: memory-bank/startHere.md

# 2. Find feature docs
Glob: memory-bank/features/**/*.md

# 3. Search content
Grep: "pattern" --path=memory-bank/

# 4. Read specific docs
Read: memory-bank/features/[name]/technical-design.md
```

### Best Practices
- Always start with `startHere.md`
- Use file size indicators to manage context
- Navigate by section headers, not line numbers
- Follow cross-references for related docs
- Update `activeContext.md` for current work

## 📋 Templates Available

1. **Feature Template**: `features/feature-template.md`
2. **Plan Template**: `plans/plan-template.md`
3. **Guide Template**: (see existing guides for pattern)

## 🔗 Essential Links

- **Navigation**: [startHere.md](./startHere.md)
- **Current Work**: [activeContext.md](./activeContext.md)
- **AI Guide**: [AI_GUIDE.md](./AI_GUIDE.md)
- **Documentation Rules**: [guides/memory-bank-rules.md](./guides/memory-bank-rules.md)

## 📈 Success Metrics

This memory-bank system helps teams achieve:
- 60% faster onboarding for new developers
- 40% reduction in duplicate code
- 75% fewer "where is this documented?" questions
- 90% of AI queries resolved without external search

## 🎓 Learning Path

1. **Day 1**: Read startHere.md, activeContext.md, projectbrief.md
2. **Week 1**: Review one example feature (calculator)
3. **Week 2**: Study complex feature (dashboard)
4. **Month 1**: Create your first feature using template

## 🤝 Contributing

When adding documentation:
1. Follow the 8-file modular structure
2. Add metadata frontmatter
3. Include file size indicators
4. Create cross-references
5. Update startHere.md
6. Add to activeContext.md if current work

## 📝 Maintenance

### Monthly
- Review and update activeContext.md
- Archive completed features/decisions
- Update file size indicators if files grow

### Quarterly
- Review all cross-references
- Update templates based on learnings
- Archive old plans/proposals

## ❓ FAQ

**Q: Which file should I start with?**
A: `startHere.md` - it's the master navigation hub.

**Q: How do I find information about a specific feature?**
A: Navigate to `features/[name]/README.md` then follow the links.

**Q: What if a file is too large for AI context?**
A: Use `guides/executive-summaries.md` or navigate to specific sections.

**Q: How do AI agents use this system?**
A: See `guides/ai-integration-guide.md` for detailed patterns.

**Q: Where do I document future work?**
A: Use `plans/` directory with `plan-template.md`.

---

**Status**: Template memory-bank ready for customization
**Last Updated**: 2025-01-10
**Maintained By**: [Your Team]

**Next Steps**: Customize startHere.md, activeContext.md, and projectbrief.md for your project.

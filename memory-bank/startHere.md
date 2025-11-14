---
owner: [Project Owner]
last_updated: 2025-11-10
size: 🟢
status: template
sources_of_truth: [startHere.md]
related_files: [activeContext.md, projectbrief.md, progress.md, AI_GUIDE.md, ceo-dashboard.md, tools/memory_rag/README.md]
---

# 🎯 Start Here: Memory-Bank + MBIE Navigation Hub

**Purpose:** Master navigation hub for your consulting deployment toolkit with semantic search intelligence
**Status:** Production-ready template (customize for your client/project)
**File Count:** Core files + guides + features + MBIE tool
**Latest Update:** PR #9 merged - MBIE extraction complete, CI removed, local validation active

## 🔥 Most-Used Paths (Top 5)

Customize these paths for your project's most frequent navigation needs:

1. **🎯 CEO Dashboard** → `ceo-dashboard.md` 🟢 (Real-time project status and next actions)
2. **Current Focus** → `activeContext.md#current-focus` (Strategic context)
3. **Project Overview** → `projectbrief.md` 🟢 (Core goals and scope)
4. **Technical Stack** → `techContext.md#technology-stack` 🟡 (Tech details)
5. **Implementation Status** → `progress.md` 🟡 (What works, what's left)

## 📁 File Size Guide for AI Context Optimization

🟢 **AI-Friendly Files** (<400 lines) - Use directly in AI context
🟡 **Large Files** (400-600 lines) - Start with executive summary, use ## sections
🔴 **Very Large Files** (>600 lines) - ALWAYS start with executive summary from `guides/executive-summaries.md`

## 🚀 Quick Navigation by Task

### 🎯 Getting Started
- **🎯 CEO Dashboard**: `ceo-dashboard.md` 🟢 (Real-time project status - START HERE for daily operations)
- **📁 Projects Hub**: `projects/README.md` 🟢 (Standard + Enhanced project structures, templates, organization patterns)
- **Project Overview**: `projectbrief.md` 🟢 (Core goals, scope, success metrics)
- **Current Focus**: `activeContext.md` 🟡 (Strategic context, detailed status, current priorities)
- **Why This Exists**: `productContext.md` 🟢 (Product vision and user needs)
- **Executive Summary**: `executiveSummary.md` 🟢 (High-level project overview)

### 🏗️ Technical Implementation
- **Architecture Patterns**: `systemPatterns.md` 🟡 (Design decisions and patterns)
- **Tech Stack & Setup**: `techContext.md` 🟡 (Technology stack, development environment)
- **Implementation Status**: `progress.md` 🟡 (Current progress, what works, what's left)
- **AI Optimization**: `AI_GUIDE.md` 🟢 (Efficient AI assistant usage patterns)

### 🛠️ Tools & Infrastructure
- **MBIE (Memory-Bank Intelligence Engine)**: `features/mbie/README.md` 🟢 (Semantic search and documentation retrieval)
  - Requirements: `features/mbie/requirements.md` 🟢 (What MBIE accomplishes)
  - Technical Design: `features/mbie/technical-design.md` 🟡 (Architecture and system design)
  - Implementation: `features/mbie/implementation.md` 🟡 (Installation and API guide)
  - Testing: `features/mbie/testing-strategy.md` 🟢 (Test approach and validation)

### 📋 Feature Development
Browse `features/` directory for detailed feature documentation with 3 complete examples:

**Simple Feature Pattern** (⏱️ 4-6 hours):
- **Example Calculator**: `features/example-calculator/README.md` 🟢
  - Basic component structure, state management, pure functions
  - Unit testing patterns, accessibility basics
  - ~500 lines total code

**Complex Feature Pattern** (⏱️ 4-6 weeks):
- **Example Dashboard**: `features/example-dashboard/README.md` 🟢
  - Real-time data, WebSocket integration, advanced state management
  - Performance optimization, virtualization, code splitting
  - ~5,000 lines total code

**Integration Pattern** (⏱️ 2-3 weeks):
- **Example API Integration**: `features/example-api-integration/README.md` 🟢
  - External API patterns, OAuth, retry logic, circuit breakers
  - Webhook handling, idempotency, rate limiting
  - ~2,000 lines total code

Each feature follows the 8-file modular structure:
```
features/[name]/
  README.md            - 🟢 Navigation hub (50 lines)
  requirements.md      - 🟢 User stories & acceptance criteria (100-200 lines)
  user-experience.md   - 🟡-🔴 UX flows & interactions (200-500 lines)
  technical-design.md  - 🟡-🔴 Architecture & business logic (300-800 lines)
  implementation.md    - 🟡-🔴 Step-by-step code guide (400-700 lines)
  content-strategy.md  - 🟡-🔴 UI copy & error messages (200-500 lines)
  testing-strategy.md  - 🟢-🟡 Test scenarios & coverage (150-300 lines)
  decisions.md         - 🟢-🟡 Key decisions & rationale (100-200 lines)
  dependencies.md      - 🟢 Libraries & versions (100 lines)
```

### 🤖 AI Optimization & Documentation
- **AI Assistant Guide**: `AI_GUIDE.md` 🟢 (Efficient context usage, smart search patterns)
- **AI Integration Guide**: `guides/ai-integration-guide.md` 🟢 (AI tool workflows, patterns)
- **Subagent Collaboration**: `guides/subagent-collaboration-guide.md` 🟢 (Human-AI & AI-AI coordination)
- **Executive Summaries**: `guides/executive-summaries.md` 🟢 (Required for 🔴 large files)
- **Documentation Framework**: `guides/documentation-framework.md` 🔴 (Use sections: `## File Size Categories`)
- **Memory-Bank Rules**: `guides/memory-bank-rules.md` 🟢 (Update protocols, workflows)

### 📁 Supporting Infrastructure
- **Projects Directory**: `projects/README.md` 🟢 (Standard vs Enhanced structures, templates for client/internal projects)
- **Archive**: `archive/README.md` 🟢 (Deprecated docs, archiving guidelines)
- **Plans**: `plans/README.md` 🟢 (Future work, proposals, planning documents)
- **Plan Template**: `plans/plan-template.md` 🟢 (Template for new proposals)

### 📊 Project Management
- **Current Status**: `ceo-dashboard.md` 🟢 (5-second scan of all active work)
- **Strategic Context**: `activeContext.md` 🟡 (Detailed status, milestones, focus areas)
- **Planning Docs**: `../docs/plans/` (Detailed planning documents)

## 📊 Current Status Overview

### Current Phase: Production-Ready Deployment (Nov 2025)
- [x] MBIE extracted from personal repo to Template
- [x] All 121 tests passing (10 intentionally skipped)
- [x] CI/CD removed - replaced with local validation workflow
- [x] Validation script created: `scripts/validate-before-deployment.sh`
- [x] MBIE tested and fully operational

### Current Outcomes
- **Test Suite Status**: 121/121 passing (100%)
- **MBIE Functionality**: Fully operational semantic search engine
- **Deployment Validation**: Ready for client deployment
- **SleekAI Case Study**: 90% founder time reduction (5 hrs/week → 30 min/week)

## 🎯 Task-Specific Navigation Paths

### Understanding Project's Current Focus
```
1. activeContext.md → ## Current Focus
2. projectbrief.md → ## Success Metrics
3. progress.md → ## What Works, What's Left
```

### Technical Implementation & Architecture
```
1. systemPatterns.md → ## Architecture Patterns
2. techContext.md → ## Technology Stack
3. features/[name]/technical-design.md → ## Business Logic
4. features/[name]/implementation.md → ## Code Guidance
```

### Feature Planning & Development
```
1. features/[name]/README.md (feature navigation hub)
2. features/[name]/requirements.md (user objectives)
3. features/[name]/user-experience.md (UX flows)
4. features/[name]/technical-design.md (business logic)
5. features/[name]/implementation.md (code guidance)
```

### AI Context Optimization
```
1. AI_GUIDE.md → ## File Size Guide
2. AI_GUIDE.md → ## Smart Search Patterns
3. guides/executive-summaries.md (for 🔴 large files)
4. guides/documentation-framework.md → ## AI Navigation System
```

### Tools & Infrastructure Implementation
```
1. features/mbie/README.md (MBIE navigation hub)
2. features/mbie/requirements.md (objectives and user stories)
3. features/mbie/technical-design.md → ## System Architecture
4. features/mbie/implementation.md → ## Installation Steps
5. features/mbie/testing-strategy.md → ## Testing Approach
```

## 🧠 AI Context Optimization Rules

### ✅ Efficient AI Usage
- Start with this file (startHere.md) for navigation
- Use file size indicators (🔴🟡🟢) to guide context loading
- Search by section headers (`## Section Name`)
- Follow task-specific navigation paths
- Combine related 🟢 files together

### ❌ Avoid These Patterns
- Loading multiple complete 🔴 files simultaneously
- Using line numbers instead of section headers
- Mixing unrelated documentation contexts
- Ignoring file size categorization

## 📈 Success Metrics

Customize these metrics for your project:

### Project Metrics
- **[Metric Category 1]**: [Target value]
- **[Metric Category 2]**: [Target value]
- **[Metric Category 3]**: [Target value]

### Quality Indicators
- Reduced development time for common tasks
- Improved code quality and maintainability
- Better team collaboration and knowledge sharing
- Enhanced AI assistant efficiency

## 🔄 Next Actions

Customize with your project's immediate next steps:

### Immediate Next Steps
1. [ ] [Action item 1]
2. [ ] [Action item 2]
3. [ ] [Action item 3]

### Upcoming Milestones
- **[Milestone 1]**: [Description and timeline]
- **[Milestone 2]**: [Description and timeline]
- **[Milestone 3]**: [Description and timeline]

---

## 📋 Using This Template for Your Project/Client

**For your first client deployment:**
1. Clone this Template to their environment: `git clone Template.git [ClientName]-transformation`
2. Customize all `[Project Name]` and `[Project Owner]` placeholders
3. Update `projectbrief.md` with their business goals
4. Update `ceo-dashboard.md` with active projects/initiatives
5. Run `./scripts/validate-before-deployment.sh` to validate
6. Deploy MBIE and start client discovery: `cd tools/memory_rag && python3 cli.py index --full`

**MBIE for Client Discovery:**
Use MBIE semantic search to identify automation opportunities:
```bash
cd tools/memory_rag
python3 cli.py query "manual approval processes"
python3 cli.py query "founder bottleneck"
python3 cli.py query "time consuming weekly"
```

**Current Focus**: This is a production-ready template for consulting deployments. Customize it for your specific client/project and use MBIE for rapid business intelligence discovery.

**Navigation Tip**: Use the file size indicators (🔴🟡🟢) to optimize AI context loading. Always start with startHere.md, then follow task-specific navigation paths.

# Guide: Comprehensive Documentation & AI Navigation Framework

**Version:** 3.0
**Last Updated:** 2025-12-06
**Status:** Complete Framework - Domain-Driven Documentation + AI Navigation System

This document is the **single source of truth** for creating, maintaining, and navigating documentation within the NoCapLife Coach project. It combines the **Domain-Driven Documentation** approach for feature specifications with the **AI Navigation System** for optimal AI assistant efficiency and human developer experience.

## Overview: Dual-Layer Documentation System

Our documentation framework operates on two complementary layers:

1. **Content Layer**: Domain-driven modular documentation for features and specifications
2. **Navigation Layer**: AI-optimized navigation system for efficient context usage

This dual approach ensures documentation scales effectively from solo development to 1M+ users while maintaining optimal AI assistant performance.

## Part I: AI Navigation System

### Core Navigation Files (Required for All Projects)

#### startHere.md (Master Navigation Hub)
- **Purpose:** Primary entry point when AI loads entire memory bank
- **Location:** `memory-bank/startHere.md`
- **Content Requirements:**
  - File size categorization system (🔴🟡🟢)
  - Task-specific navigation paths
  - Directory structure guide
  - Performance guidelines
- **Maintenance:** Update navigation paths when adding new features or major files

#### executive summary at the top of the file (Large File Optimization)
- **Purpose:** Context-optimized summaries for files >600 lines
- **Location:** at the top of large files
- **Content Requirements:**
  - Section-based navigation using `## Section Name` format
  - Key APIs/interfaces for each large file
  - Integration points and dependencies
  - Quick navigation instructions for AI
- **Maintenance:** Add new summaries when files exceed 600 lines

#### AI_GUIDE.md (AI Assistant Instructions)
- **Purpose:** Detailed AI optimization guide and usage patterns
- **Location:** `memory-bank/AI_GUIDE.md`
- **Content Requirements:**
  - File size guide with context optimization
  - Smart search patterns by task type
  - Context layering strategies
  - Performance tips and success metrics
- **Maintenance:** Update when changing file organization or adding new patterns

### File Size Categorization System

All documentation files must be categorized for AI context optimization:

```
🟢 AI-Friendly Files (<400 lines)
- Use directly in AI context
- Combine multiple related files
- Examples: calculator specs, small guides

🟡 Large Files (400-600 lines)
- Start with executive summary
- Use specific sections by ## headers
- Examples: technical architecture, roadmaps

🔴 Very Large Files (>600 lines)
- ALWAYS start with executive summary
- Section-based navigation required
- Examples: implementation specs, content strategies
```

### Section-Based Navigation Standards

All files >300 lines must use standardized section headers:

```markdown
## Authentication Architecture
## Database Schema
## Component Architecture
## UI Copy & Messaging
## Business Logic Engine
## Integration Patterns
## Primary User Flow
## Error & Edge Cases
```

**Navigation Format:** Search using `## Section Name` (not line numbers)
**Stability:** Section headers are stable; line numbers change frequently

### File Purpose Headers (Required for All Files >200 lines)

```markdown
**Purpose:** What this file accomplishes
**When to use:** Specific scenarios for referencing this file
**Quick sections:** Key ## headers for navigation
**Size:** 🔴/🟡/🟢 indicator
```

## Part II: Domain-Driven Documentation Structure

### Core Problem Statement

Our previous documentation approach resulted in monolithic specification files that became difficult for AI assistants to process accurately and efficiently. Large files led to:
- Incomplete context processing
- Increased errors in updates
- Difficulty in maintaining specific sections
- Poor discoverability of information
- Reduced collaboration efficiency

### Framework Principles (MIMIC + Navigation)

- **Modular:** Features represented by self-contained folders, not single files
- **Manifest-Driven:** Each feature folder contains central README.md navigation hub
- **Concerns-Separated:** Information organized into specialized files by functional domains
- **Section-Navigable:** All files use standardized ## headers for AI navigation
- **Size-Optimized:** File size categories guide AI context usage

### Standard Feature Documentation Structure

Every feature should be documented using this standardized folder structure:

```
memory-bank/
  startHere.md                    # 🎯 Master navigation (always start here)
  AI_GUIDE.md                     # 🤖 AI optimization guide
  guides/
    executive summary at the top of the file        # 📋 Large file summaries (critical for 🔴 files)
    documentation-framework.md    # 📚 This file - source of truth
    ui-component-library-guide.md # 🎨 UI component standards
  features/
    [feature-name]/
      README.md                   # Overview and navigation hub (🟢)
      requirements.md             # User objectives and acceptance criteria (🟢)
      user-experience.md          # Complete UX flow and interactions (🟡/🔴)
      technical-design.md         # Data models, logic rules, and architecture (🟡/🔴)
      implementation.md           # File structure, API specs, and code guidance (🔴)
      content-strategy.md         # UI copy, messaging, and external resources (🔴)
      testing-strategy.md         # Test scenarios and validation approach (🟡)
      decisions.md                # Key decisions, trade-offs, and rationale (🟢/🟡)
  feature-specs/                  # Legacy and infrastructure specs
    Apps/                         # Calculator specifications (🟢)
    supabase-setup.md            # Infrastructure setup (🔴)
    home-page-spec.md            # Main page specification (🟡)
```

### File-Specific Guidelines with AI Optimization

#### README.md (Navigation Hub) - Target: 🟢 <100 lines
- **Purpose:** Central index providing quick overview and navigation
- **AI Usage:** Primary entry point for feature context
- **Content:**
  - Feature summary (2-3 sentences)
  - Current status and file size indicators
  - Quick links to other files with brief descriptions
  - Key stakeholders and contacts
- **Section Headers:** Use when >50 lines

#### requirements.md (User Objectives) - Target: 🟢 100-200 lines
- **Purpose:** Define what the feature accomplishes and why
- **AI Usage:** Business context and acceptance criteria
- **Content:**
  - User stories and acceptance criteria
  - Business objectives and success metrics
  - Scope boundaries (what's included/excluded)
  - Priority levels and phasing
- **Section Headers:** `## User Stories`, `## Acceptance Criteria`, `## Business Objectives`

#### user-experience.md (UX Flow) - Target: 🟡 150-400 lines
- **Purpose:** Detailed user journey and interaction design
- **AI Usage:** UX patterns and flow reference
- **Required Sections:**
  ```
  ## Primary User Flow
  ## Interactive Components
  ## Error & Edge Cases
  ## Accessibility Considerations
  ```
- **AI Navigation:** Start with `## Primary User Flow` for main patterns

#### technical-design.md (System Architecture) - Target: 🟡 200-500 lines
- **Purpose:** Technical foundation and business logic
- **AI Usage:** System architecture and integration patterns
- **Required Sections:**
  ```
  ## Data Models & Types
  ## Business Logic Engine
  ## Component Architecture
  ## Integration Architecture
  ```
- **Logic Description:** Use clear, structured plain English with examples
- **AI Navigation:** Search specific sections for focused context

#### implementation.md (Development Guide) - Often 🔴 >600 lines
- **Purpose:** Concrete implementation guidance
- **AI Usage:** File structure, API specs, development guidance
- **Required Sections:**
  ```
  ## Component Architecture
  ## Data Flow & State Management
  ## API Integration
  ## File Organization
  ```
- **AI Navigation:** ALWAYS use executive summary first
- **Content:** File structure, API specifications, integration requirements

#### content-strategy.md (Copy and Messaging) - Often 🔴 >600 lines
- **Purpose:** All user-facing content and external resources
- **AI Usage:** UI copy, messaging frameworks, content standards
- **Required Sections:**
  ```
  ## Display Labels & Categories
  ## Educational Content Library
  ## UI Copy & Messaging
  ## Medical Citations & Sources
  ```
- **AI Navigation:** ALWAYS use executive summary first
- **Content:** UI copy, help text, external resources, personalization rules

#### testing-strategy.md (Quality Assurance) - Target: 🟡 100-400 lines
- **Purpose:** Validation approach and test scenarios
- **AI Usage:** Test implementation guidance
- **Required Sections:**
  ```
  ## Test Cases & Scenarios
  ## Edge Case Handling
  ## Performance Testing
  ## User Acceptance Testing
  ```

#### decisions.md (Decision Log) - Target: 🟢-🟡 50-300 lines (grows over time)
- **Purpose:** Record key decisions and rationale
- **AI Usage:** Context for architectural choices
- **Content:** Architecture decision records (ADRs), trade-offs, technical debt
- **Section Headers:** `## [Decision Date] - [Decision Title]`

## Part III: AI Navigation Workflows

### Task-Specific Navigation Paths

#### Building Features
```
1. startHere.md (navigation)
2. executive summary at the top of the file (if working with 🔴 files)
3. feature-specs/Apps/[similar-calculator].md (reference implementation)
4. guides/ui-component-library-guide.md (UI patterns)
```

#### Database/Infrastructure Work
```
1. executive summary at the top of the file (supabase summary)
2. feature-specs/supabase-setup.md → search "## Database Schema"
3. systemPatterns.md (data patterns)
```

#### Authentication/User Flow
```
1. feature-specs/supabase-setup.md → search "## Authentication Architecture"
2. features/cholesterol-insights/user-experience.md → search "## Primary User Flow"
3. features/cholesterol-insights/implementation.md → search "## API Integration"
```

#### UI/UX Development
```
1. executive summary at the top of the file (UX summary)
2. features/cholesterol-insights/content-strategy.md → search "## UI Copy & Messaging"
3. guides/ui-component-library-guide.md (component patterns)
```

### Context Optimization Rules

#### Efficient AI Usage (✅ Do This)
- Start with startHere.md for full memory bank loads
- Use executive summary at the top of the file first for 🔴 files
- Search by section headers (`## Section Name`)
- Combine related 🟢 files together
- Follow task-specific navigation paths

#### Inefficient AI Usage (❌ Avoid This)
- Loading multiple complete 🔴 files
- Using line numbers instead of section headers
- Mixing unrelated documentation
- Ignoring file size indicators
- Including historical/archive content unnecessarily

## Part IV: Implementation & Maintenance

### For New Features

1. **Create folder structure** using standard template
2. **Start with README.md** for overview and navigation
3. **Develop requirements.md** before implementation begins
4. **Build other files iteratively** as feature develops
5. **Add to executive summary at the top of the file** if any file exceeds 600 lines
6. **Update startHere.md** navigation paths if needed

### For Large File Management

#### When File Exceeds 400 Lines (🟡 Threshold)
1. Add standardized section headers
2. Include file purpose header
3. Consider splitting if file serves multiple concerns

#### When File Exceeds 600 Lines (🔴 Threshold)
1. **Required:** Add summary to executive summary at the top of the file
2. **Required:** Standardized section headers
3. **Required:** File purpose header
4. **Evaluate:** Split into sub-files if serving multiple concerns

#### Sub-file Strategy
Create subfolders when splitting large files:
```
technical-design/
  data-models.md
  business-logic.md
  architecture.md
README.md (updated with navigation to sub-files)
```

### Section Header Standards

Maintain consistency across all documentation:

```markdown
## Authentication Architecture     # For auth-related content
## Database Schema                # For database structure
## Component Architecture         # For React/UI components
## Data Flow & State Management   # For state and data handling
## API Integration               # For backend integration
## Business Logic Engine         # For business rules and algorithms
## UI Copy & Messaging           # For user-facing content
## Primary User Flow             # For main user journey
## Error & Edge Cases            # For error handling
## File Organization             # For project structure
## Integration Patterns          # For system integration
## Performance Considerations    # For optimization
## Testing Strategy              # For test planning
## Security Considerations       # For security measures
```

### Cross-File Linking Strategy

- **Feature-internal links:** `[See UX Flow](./user-experience.md#primary-user-flow)`
- **Cross-feature links:** `[Related Feature](../other-feature/README.md)`
- **Code references:** `[Implementation](../../src/components/FeatureName.tsx)`
- **Navigation references:** `[Navigation Guide](../../startHere.md#building-features)`

### Code Comment Integration

#### Enhanced TSDoc/JSDoc with Navigation
```typescript
/**
 * Orchestrates the full analysis for Cholesterol Insights feature.
 * @see memory-bank/features/cholesterol-insights/technical-design.md#business-logic-engine
 * @navigation Use startHere.md → "Building Features" path for context
 * @param data User input data
 * @returns Complete analysis result
 */
```

#### Business Logic References
```typescript
/**
 * Maps categories to display labels per business rules.
 * Business logic: memory-bank/features/cholesterol-insights/technical-design.md#business-logic-engine
 * Decisions: memory-bank/features/cholesterol-insights/decisions.md#display-mapping
 * @param category Clinical category
 * @returns User-friendly display label
 */
```

## Part V: Quality Assurance & Maintenance

### Weekly Maintenance Tasks
1. **Verify navigation paths** with sample AI tasks
2. **Check section headers** match executive summaries
3. **Update file size indicators** if major changes occurred
4. **Test AI navigation** with common workflows

### Monthly Maintenance Tasks
1. **Review file sizes** and update categorization (🔴🟡🟢)
2. **Validate cross-file links** and fix broken references
3. **Update executive summaries** for significantly changed files
4. **Assess navigation path efficiency** and optimize

### Quarterly Maintenance Tasks
1. **Complete framework review** and updates
2. **AI performance assessment** and optimization
3. **File organization evaluation** and restructuring if needed
4. **Team feedback integration** and process improvements

### Success Metrics

#### Quantitative Goals
- **Context Efficiency:** 50% reduction in tokens for same tasks
- **Navigation Speed:** 75% faster information discovery
- **Maintenance Overhead:** Zero line number updates needed
- **File Organization:** 90% of files under target size categories

#### Qualitative Indicators
- AI finds relevant information quickly
- Implementation follows existing patterns
- Architecture constraints are respected
- Code quality remains high
- No context overflow issues
- New team members onboard efficiently

## Part VI: Migration Strategy

### For Existing Large Files
1. **Assessment:** Identify files >400 lines needing migration
2. **Section Headers:** Add standardized ## headers
3. **Executive Summaries:** Create summaries for 🔴 files
4. **Navigation Updates:** Update startHere.md and AI_GUIDE.md
5. **Validation:** Test AI navigation efficiency

### For New Team Members
1. **Start with startHere.md** for project overview
2. **Review AI_GUIDE.md** for efficient documentation usage
3. **Follow task-specific paths** from startHere.md
4. **Reference this framework** for documentation standards

This comprehensive framework ensures documentation scales effectively while maintaining optimal AI assistant performance and human developer experience. It serves as the single source of truth for all documentation practices in the NoCapLife Coach project.
---

## Part III: Project Directory Patterns

### Overview

Projects are documented using one of two structures depending on complexity, scale, and execution timeline. This dual-structure approach enables efficient organization from single-phase client projects to multi-year strategic initiatives.

### Standard Project Structure (Most Projects)

**Use for:** Client delivery, product development, operational improvements

```
projects/[project-name]/
├── README.md           # Navigation hub and quick reference
├── context.md          # Detailed project context
├── CHANGELOG.md        # Weekly learning record
├── decisions.md        # Key decisions and rationale
├── progress.md         # Implementation progress tracking
└── [additional docs]   # Project-specific documentation
```

**Characteristics:**
- Documentation typically <20K words
- Single-phase execution with clear start/end
- Direct client engagement or internal development
- Standard weekly tracking via CHANGELOG.md

**Example Projects:**
- Client transformation and consulting engagements
- SaaS product features and integrations
- Internal automation and tooling projects
- VA hiring and delegation systems

**Template Location:** `projects/example-templates/standard-project/`

### Enhanced Project Structure (Complex Multi-Phase Projects)

**Use for:** Strategic initiatives with extensive documentation, validation, and coordination needs

```
projects/[project-name]/
├── README.md           # Executive summary and navigation hub
├── CHANGELOG.md        # Weekly progress, decisions, insights
├── strategy/           # PLANNING documents (what to do)
│   ├── README.md      # Strategy directory guide
│   ├── [main-strategy].md
│   ├── [implementation-plans].md
│   └── [financial-models].md
├── analysis/           # PROOF documents (why it works)
│   ├── README.md      # Analysis directory guide
│   ├── [expert-analysis].md
│   ├── [ai-comparisons].md
│   └── [due-diligence].md
└── coordination/       # EXECUTION documents (how to track)
    ├── README.md      # Coordination directory guide
    ├── [issue-templates].md
    ├── [meeting-agendas].md
    └── [milestone-tracking].md
```

**When to Use Enhanced Structure:**
- ✅ Projects with 20K+ words of strategy documentation
- ✅ Multiple expert analyses or AI validation needed (board reviews, AI comparisons)
- ✅ Multi-phase execution spanning 2+ years (Phase 1 → Phase 2 → Phase 3)
- ✅ Partnership or joint venture structures requiring extensive coordination
- ✅ Complex deal flow with multiple sourcing strategies
- ✅ Strategic initiatives requiring validation before execution

**Example Projects:**
- Private equity acquisition strategies
- Multi-year partnership ventures
- Complex M&A initiatives
- Strategic business pivots with Board approval

**Template Location:** `projects/example-templates/enhanced-project/`

### File Placement Decision Guide

#### strategy/ Directory (Planning Documents)
**Purpose:** Define what to do and how to execute

**Contains:**
- Acquisition strategies and comprehensive business plans
- Deal sourcing playbooks and go-to-market strategies
- Financial models, projections, and ROI scenarios
- Implementation blueprints and execution roadmaps
- Partnership structures and operating rhythms

**File Characteristics:**
- Typically 🔴 (>600 lines) for comprehensive strategies
- Requires executive summaries
- Section-based navigation essential
- Read during: Planning phases, strategic pivots, partner alignment

#### analysis/ Directory (Validation Documents)
**Purpose:** Prove why the strategy will work

**Contains:**
- Expert board analysis and consensus reports
- AI model comparisons (Claude vs Gemini multi-model validation)
- Due diligence reports and market research
- Competitive assessments and feasibility studies
- Risk analysis and mitigation strategies

**File Characteristics:**
- Typically 🟢 (<400 lines) for focused analyses
- Data-driven with clear conclusions
- Objective validation and second opinions
- Read during: Decision validation, risk assessment, board reviews

#### coordination/ Directory (Execution Documents)
**Purpose:** Track execution and coordinate multi-party work

**Contains:**
- GitHub issue templates and sprint planning materials
- Meeting agendas and partnership coordination docs
- Milestone checklists and phase-by-phase tracking
- Weekly sync formats and status report templates
- Partnership agreement templates and legal structures

**File Characteristics:**
- Typically 🟢 (<400 lines) for operational docs
- Action-oriented with clear ownership
- Easy to scan for next actions
- Read during: Sprint execution, milestone tracking, coordination meetings

### CHANGELOG.md for Projects

**Purpose:** Weekly learning record capturing decisions, insights, and pivots

**Required Elements:**
- Week header with date range
- Key Learning (1-2 sentences maximum)
- Strategic Pivot (if applicable, From → To format)
- Wins (bullet list, 3-5 maximum)
- Next Steps (action items with clear owners)
- Status Change (if project phase shifted)
- Metrics (optional, only if directly relevant)

**Update Triggers:**
- Weekly meetings completed
- Strategic pivots occur
- Key learnings discovered
- Major milestones achieved
- Status changes happen

**Rule of Thumb:** "Would you want to remember this when planning next quarter?" → Yes = Update

### Decision Tree: Which Structure to Use?

```
Start: New project needs documentation structure

├─ Is documentation >20K words?
│  ├─ YES → Consider Enhanced Structure
│  │  ├─ Multiple expert analyses needed? → Enhanced
│  │  ├─ Multi-phase execution (2+ years)? → Enhanced
│  │  ├─ Partnership/JV coordination? → Enhanced
│  │  └─ Single client delivery? → Standard
│  │
│  └─ NO → Standard Structure
│     ├─ Client delivery project → Standard
│     ├─ Product feature development → Standard
│     ├─ Operational improvement → Standard
│     └─ Internal tooling → Standard

Result: Clear structure choice based on objective criteria
```

### Project Template Usage

**Copy Standard Template:**
```bash
cp -r memory-bank/projects/example-templates/standard-project/ \
      memory-bank/projects/[your-project-name]/
```

**Copy Enhanced Template:**
```bash
cp -r memory-bank/projects/example-templates/enhanced-project/ \
      memory-bank/projects/[your-project-name]/
```

**Customize:**
1. Update README.md with project specifics
2. Rename [placeholder].md files appropriately
3. Add your actual strategy/analysis/coordination documents
4. Update cross-references in memory-bank core files
5. Add project to ceo-dashboard.md and activeContext.md

### Integration with Core Memory-Bank

Projects integrate with core memory-bank files:

**ceo-dashboard.md** - Real-time project status (5-second scan)
**activeContext.md** - Strategic context and detailed status
**startHere.md** - Navigation to projects directory
**projects/README.md** - Complete project catalog

**Update Flow:**
1. Project status changes → Update project's README.md or context.md
2. Major milestones → Update CHANGELOG.md
3. Next actions → Update ceo-dashboard.md
4. Strategic changes → Reference in activeContext.md

---

**See Also:**
- [projects/README.md](../projects/README.md) - Complete project organization guide
- [startHere.md](../startHere.md) - Master navigation hub
- [memory-bank-rules.md](./memory-bank-rules.md) - Update protocols and workflows

---
owner: Randy
last_updated: 2025-11-14
size: 🟢
status: active
sources_of_truth: [projectbrief.md]
related_files: [productContext.md, activeContext.md, progress.md, tools/memory_rag/README.md, CLAUDE.md]
---

# Project Brief: Randy Questions Bot

**Purpose:** Slack-based Q&A system for content team to query Randy's Personal repo knowledge base
**Status:** Active - Template-based implementation with read-only MBIE access
**Created:** November 14, 2025 (Issue #505)

## Project Overview

### What is This Project?

**Randy Questions Bot** is a Slack-based Q&A interface that allows whitelisted content team members (Sebastian, etc.) to ask questions about Randy's business philosophy, strategies, and methodologies by querying the Personal repo's memory-bank via MBIE semantic search - **WITHOUT write access to the Personal repo**.

**Key Features:**
- Slack channel: `#randy-questions`
- MBIE-powered semantic search of Personal repo
- Read-only enforcement via CLAUDE.md instructions
- Whitelist-based access control
- Source citations for all answers

### Why Does This Project Exist?

**Problem Statement:**
Content team members need to understand Randy's business philosophy, Anti-Rat Race principles, and client transformation methodologies to create compelling content. However, giving direct access to the Personal repo creates risk of accidental modifications to critical business documentation.

**Solution Approach:**
This project provides:
1. **Read-Only Access**: MBIE queries Personal repo without write permissions
2. **Natural Language Q&A**: Content team asks questions in Slack, gets AI-powered answers
3. **Source Attribution**: All answers cite specific memory-bank files for verification
4. **Whitelist Security**: Only authorized content team members can access

**Value Proposition:**
- **For Content Team**: Instant access to Randy's knowledge base without needing to navigate complex repo structure
- **For Randy**: Zero risk of accidental changes to Personal repo while enabling team to leverage his documented expertise
- **For Business**: Scales Randy's knowledge to content creation without bottlenecking on his direct involvement

## Core Objectives

### Primary Goals

1. **Enable Content Team Q&A via Slack**
   - **Description:** Content team can ask natural language questions in #randy-questions Slack channel
   - **Success Metric:** ✅ Slack integration configured, whitelisted users can interact
   - **Status:** Pending Slack channel creation

2. **MBIE Semantic Search of Personal Repo**
   - **Description:** Local MBIE instance queries Personal/memory-bank/ and related sources
   - **Success Metric:** ✅ MBIE indexed 400+ files from Personal repo
   - **Status:** In progress (indexing running)

3. **Read-Only Enforcement**
   - **Description:** Zero write access to Personal repo files via CLAUDE.md instructions
   - **Success Metric:** ✅ CLAUDE.md configured with mandatory read-only rules
   - **Status:** Complete

4. **Source Attribution**
   - **Description:** All answers cite specific Personal repo file paths
   - **Success Metric:** Response template includes source citations
   - **Status:** Complete (template in CLAUDE.md)

### Secondary Goals

- [x] Configure MBIE domains for Anti-Rat Race content (boost: 2.5x)
- [x] Create .env whitelist configuration
- [x] Document system in randy-questions memory-bank
- [ ] Test query: "What common wisdom does Randy contradict?"
- [ ] Deploy to Slack for content team access

## Project Scope

### In Scope

**Core Features:**
- [Feature 1 - brief description]
- [Feature 2 - brief description]
- [Feature 3 - brief description]

**Core Capabilities:**
- [Capability 1]
- [Capability 2]
- [Capability 3]

**Deliverables:**
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

### Out of Scope

**Explicitly Excluded:**
- [Excluded item 1 - why it's out of scope]
- [Excluded item 2 - why it's out of scope]
- [Excluded item 3 - why it's out of scope]

**Future Considerations:**
- [Future enhancement 1]
- [Future enhancement 2]

## Success Metrics

### Quantitative Metrics

| Metric | Baseline | Target | Timeline | Current |
|--------|----------|--------|----------|---------|
| [Metric 1] | [Value] | [Value] | [Date] | [Value] |
| [Metric 2] | [Value] | [Value] | [Date] | [Value] |
| [Metric 3] | [Value] | [Value] | [Date] | [Value] |

### Qualitative Metrics

- **[Quality Indicator 1]**: [Description and current status]
- **[Quality Indicator 2]**: [Description and current status]
- **[Quality Indicator 3]**: [Description and current status]

### Critical Success Factors

1. **[Factor 1]**: [Why this is critical to project success]
2. **[Factor 2]**: [Why this is critical to project success]
3. **[Factor 3]**: [Why this is critical to project success]

## Project Constraints

### Timeline Constraints
- **Start Date:** [Date]
- **Target Completion:** [Date]
- **Critical Milestones:** [List key date dependencies]

### Resource Constraints
- **Team Size:** [Number of people and roles]
- **Budget:** [If applicable]
- **Technical:** [Technology limitations or requirements]

### Quality Constraints
- **Performance:** [Performance requirements]
- **Reliability:** [Uptime/availability requirements]
- **Security:** [Security requirements]
- **Accessibility:** [Accessibility requirements]

## Target Users

### Primary Users

**User Persona 1: [Name/Title]**
- **Description:** [Who they are]
- **Goals:** [What they want to achieve]
- **Pain Points:** [What problems they face]
- **How This Helps:** [How project solves their problems]

**User Persona 2: [Name/Title]**
- **Description:** [Who they are]
- **Goals:** [What they want to achieve]
- **Pain Points:** [What problems they face]
- **How This Helps:** [How project solves their problems]

### Secondary Users

- **[User Type 1]**: [Brief description and needs]
- **[User Type 2]**: [Brief description and needs]

## Assumptions & Dependencies

### Assumptions

1. **[Assumption 1]**: [What you're assuming is true]
2. **[Assumption 2]**: [What you're assuming is true]
3. **[Assumption 3]**: [What you're assuming is true]

### Dependencies

1. **[Dependency 1]**: [What this project depends on]
2. **[Dependency 2]**: [What this project depends on]
3. **[Dependency 3]**: [What this project depends on]

### Risks

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| [Risk 1] | [High/Med/Low] | [High/Med/Low] | [How to address] |
| [Risk 2] | [High/Med/Low] | [High/Med/Low] | [How to address] |
| [Risk 3] | [High/Med/Low] | [High/Med/Low] | [How to address] |

## Project Phases

### Phase 1: [Phase Name] ([Timeline])

**Objective:** [What this phase aims to achieve]

**Key Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]

**Success Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Phase 2: [Phase Name] ([Timeline])

**Objective:** [What this phase aims to achieve]

**Key Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]

**Success Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Phase 3: [Phase Name] ([Timeline])

**Objective:** [What this phase aims to achieve]

**Key Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

**Success Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Stakeholders

### Decision Makers
- **[Role/Name]**: [Responsibility and decision authority]

### Key Contributors
- **[Role/Name]**: [Contribution area]
- **[Role/Name]**: [Contribution area]

### Informed Parties
- **[Role/Name]**: [Why they need to be informed]

## Related Documentation

- **Product Context**: `productContext.md` - Why project exists, user needs
- **Active Context**: `activeContext.md` - Current status and strategic context
- **Progress Tracking**: `progress.md` - Implementation status
- **Technical Details**: `techContext.md` - Technology stack
- **System Patterns**: `systemPatterns.md` - Architecture decisions

---

**Navigation:** [Back to startHere.md](./startHere.md) | [Product Context](./productContext.md) | [Active Context](./activeContext.md)

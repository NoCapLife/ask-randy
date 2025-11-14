---
title: Subagent Collaboration Guide
type: guide
category: ai-collaboration
audience: ["developers", "ai-agents"]
last_updated: 2025-01-10
---

# Subagent Collaboration Guide

**Purpose**: Patterns for effective human-AI and AI-AI collaboration.
**Audience**: Developers working with AI assistants, AI agents coordinating work.

[← Back to Guides](./README.md)

---

## 🤖 What is a Subagent?

**Subagent**: An AI assistant (like Claude) working on a specific subtask within a larger project.

**Common Scenarios**:
- Human delegates task to AI
- AI spawns another AI instance for parallel work  
- Multiple AI agents coordinating on complex feature

## 🎯 Delegation Best Practices

### Clear Task Definition
\`\`\`
❌ Bad: "Fix the payment feature"
✅ Good: "Implement retry logic for payment API calls per memory-bank/features/payments/technical-design.md#retry-pattern"
\`\`\`

### Provide Context
Always include:
1. **What**: Specific task
2. **Where**: Relevant memory-bank paths
3. **Why**: Business context
4. **Constraints**: Deadline, dependencies, requirements

### Example Delegation
\`\`\`
Task: Implement circuit breaker for payment API

Context:
- See: memory-bank/features/payments/technical-design.md#resilience
- Current code: src/lib/payment-client.ts
- Use opossum library (already in dependencies)
- Must maintain 99.99% uptime SLA

Acceptance Criteria:
- Circuit opens after 5 failures
- Half-open state after 60s
- Tests added to payment-client.test.ts
- Update technical-design.md with implementation details
\`\`\`

## 🔄 Coordination Patterns

### Pattern 1: Sequential Handoff
\`\`\`
Agent 1: Implement feature → Update activeContext.md
Agent 2: Read activeContext.md → Add tests → Update activeContext.md
Agent 3: Review and polish → Mark complete
\`\`\`

### Pattern 2: Parallel Work
\`\`\`
Agent 1: Backend API (team/agent1/issue-123-api)
Agent 2: Frontend UI (team/agent2/issue-123-ui)
Coordinator: Integration (integration/issue-123-complete)

Sync points: Issue comments, activeContext.md updates
\`\`\`

### Pattern 3: Review & Iterate
\`\`\`
Agent 1: Initial implementation → PR
Human: Review → Feedback in PR comments
Agent 1: Address feedback → Update PR
Human: Approve → Merge
\`\`\`

## ✅ Verification Protocols

**Critical**: Always verify subagent work before relying on it.

### Verify File Creation
\`\`\`bash
# Subagent claims: "Created src/components/PaymentForm.tsx"
# Verify:
ls src/components/PaymentForm.tsx
Read: src/components/PaymentForm.tsx
\`\`\`

### Verify Test Results
\`\`\`bash
# Subagent claims: "All tests pass"
# Verify:
npm test
npm run lint
\`\`\`

### Verify Documentation Updates
\`\`\`bash
# Subagent claims: "Updated technical-design.md"
# Verify:
Read: memory-bank/features/[feature]/technical-design.md
# Check for actual changes, not just file touch
\`\`\`

## 🚨 Common Pitfalls

### Pitfall 1: Duplicate File Creation
**Problem**: Subagent creates `component-updated.tsx` instead of editing `component.tsx`

**Prevention**:
- Explicitly state: "Edit existing file, do not create new"
- Verify with `ls` before reading

### Pitfall 2: Incomplete Documentation Updates
**Problem**: Subagent says "updated docs" but only added stub

**Prevention**:
- Specify exact sections to update
- Request confirmation of specific changes made
- Verify by reading the file

### Pitfall 3: Test Failures Not Reported
**Problem**: Subagent implements feature, says "done", but tests fail

**Prevention**:
- Require test run as part of task completion
- Ask for test output, not just "tests pass"
- Run tests yourself before accepting work

## 📋 Subagent Checklist Template

Use this when delegating work:

\`\`\`markdown
## Task: [Clear, specific task description]

### Context
- Feature: memory-bank/features/[feature]/
- Current code: [file paths]
- Dependencies: [libraries, services]

### Requirements
- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Tests added/updated
- [ ] Documentation updated

### Verification
- [ ] Code compiles: \`npm run build\`
- [ ] Tests pass: \`npm test\`
- [ ] Lint passes: \`npm run lint\`
- [ ] Docs updated: [specific files]

### Deliverables
Please provide:
1. List of files created/modified
2. Test output
3. Summary of changes made
4. Any blockers or questions
\`\`\`

## 🔗 Related Documentation

- [AI Integration Guide](./ai-integration-guide.md) - AI-specific patterns
- [Testing Guide](./testing-guide.md) - Test requirements
- [Documentation Framework](../documentation-framework.md) - Doc standards

---

[← Back to Guides](./README.md)

**Human Note**: This guide helps you work effectively with AI assistants. For AI-to-AI collaboration, see ai-integration-guide.md.

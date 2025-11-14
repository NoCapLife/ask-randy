---
title: AI Integration Guide
type: guide
category: ai-development
audience: ["ai-agents", "developers"]
last_updated: 2025-01-10
---

# AI Integration Guide

**Purpose**: Generic patterns for AI tools working with this memory-bank.
**Audience**: AI agents (Claude, ChatGPT, etc.), developers integrating AI.

[← Back to Guides](./README.md)

---

## 🤖 AI Agent Workflow

### Step 1: Orient (Every Session)
\`\`\`
1. Read memory-bank/startHere.md
2. Identify relevant feature docs
3. Review activeContext.md for current work
4. Check documentation-framework.md for code comment patterns
\`\`\`

### Step 2: Research
\`\`\`
- Use Glob for file discovery
- Use Grep for content search
- Use Read for known files
- Cross-reference related docs
\`\`\`

### Step 3: Implement
\`\`\`
- Follow patterns from feature docs
- Add code comments referencing memory-bank paths
- Update tests alongside implementation
- Keep activeContext.md current
\`\`\`

### Step 4: Document
\`\`\`
- Update feature documentation if behavior changes
- Add decisions to decisions.md
- Update cross-references
\`\`\`

## 📋 Common AI Patterns

### Pattern: Feature Implementation
\`\`\`typescript
// ✅ GOOD: References memory-bank
/**
 * Process user payment
 * @see memory-bank/features/payments/technical-design.md#payment-processing
 * @see memory-bank/features/payments/implementation.md#step-3
 */
async function processPayment(order: Order): Promise<Payment> {
  // Implementation following memory-bank patterns
}
\`\`\`

### Pattern: Architecture Decision
\`\`\`
When making technical decisions:
1. Check features/[area]/decisions.md for precedent
2. If new decision, document in decisions.md
3. Reference in code comments
4. Update technical-design.md if architecture changes
\`\`\`

### Pattern: Error Investigation
\`\`\`
1. Grep for error message in codebase
2. Read relevant feature docs for context
3. Check testing-strategy.md for test patterns
4. Implement fix following established patterns
5. Add regression test
\`\`\`

## 🔗 Tool Usage Best Practices

### File Discovery
\`\`\`bash
# Find all TypeScript files in payments feature
Glob: features/payments/**/*.ts

# Find component files
Glob: components/**/*.tsx
\`\`\`

### Content Search
\`\`\`bash
# Find all references to a function
Grep: "processPayment" --type=ts

# Find configuration usage
Grep: "process\.env\.STRIPE_KEY" --type=ts
\`\`\`

### Reading Documentation
\`\`\`bash
# Always start with navigation hub
Read: memory-bank/features/[feature]/README.md

# Then read specific files as needed
Read: memory-bank/features/[feature]/technical-design.md
\`\`\`

## 🤝 Multi-Agent Collaboration

### Pattern: Coordinated Development
\`\`\`
1. Check activeContext.md for active work
2. Add your planned work to avoid conflicts
3. Use clear commit messages referencing issues
4. Update activeContext.md when completing work
\`\`\`

### Pattern: Knowledge Transfer
\`\`\`
When handing off to another agent:
1. Update activeContext.md with current state
2. Document any blockers or open questions
3. Reference relevant memory-bank docs
4. Leave clear next steps
\`\`\`

## 🔍 Quality Checklist

Before completing any task:
- [ ] Code references memory-bank navigation in comments
- [ ] Tests added/updated for changes
- [ ] Feature documentation updated if behavior changed
- [ ] activeContext.md reflects current state
- [ ] Cross-references are valid

---

[← Back to Guides](./README.md)

**AI Note**: This guide is specifically designed for AI tools. Humans may find the subagent-collaboration-guide.md more relevant for working with AI assistants.

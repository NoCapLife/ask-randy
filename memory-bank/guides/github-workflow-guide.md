# GitHub Issues Workflow Guide

**Purpose:** Optimized GitHub workflow for human-AI collaboration
**When to use:** Issue creation, project management, development workflow
**Quick sections:** Core workflows, automation scripts, best practices
**Size:** 🟢 (~290 lines)

## Overview

This guide outlines the optimized GitHub Issues workflow for AI assistants and human developers, designed for efficient collaboration with proper automation and best practices.

## Core Workflow Components

### Issue Templates
- **🚀 Feature Request** - AI-assisted feature development with complexity analysis
- **🐛 Bug Report** - Smart debugging with investigation hints  
- **⚡ Quick Task** - Sub-30-minute tasks with minimal overhead
- **📈 Enhancement** - Improvements to existing functionality
- **🔧 Refactor** - Code quality and technical debt cleanup

### Project Board
- **Columns**: Todo → In Progress → Review → Done
- **Auto-management**: Scripts handle issue assignment and updates
- **Integration**: Issues automatically linked to projects

### Labels System
- **Type**: `bug`, `feature`, `enhancement`, `refactor`, `quick-task`
- **Priority**: `high-priority`, `medium-priority`, `low-priority`
- **Status**: `needs-triage`, `in-progress`, `blocked`
- **Labels Guide**: Use consistent labeling for automation and filtering

## Essential Automation Scripts

### 1. Workflow Status & Triage
```bash
# Quick workflow overview
./scripts/github-automation/workflow-simple.sh status

# Auto-assign priorities to new issues
./scripts/github-automation/workflow-simple.sh triage
```

### 2. Feature Development Setup
```bash
# Creates branch, file structure, and TODO placeholders
./scripts/github-automation/feature-kickstart.sh [issue-number]
```

### 3. Issue Creation & Project Management
```bash
# Create issues with templates (works for both Claude Code & Cursor)
./scripts/github-automation/create-issue.sh feature "Feature name"
./scripts/github-automation/create-issue.sh bug "Bug description"
./scripts/github-automation/create-issue.sh quick "Quick task"

# Add existing issue to board  
./scripts/github-automation/project-helper.sh add [issue-number]
```

## Human-AI Collaboration Patterns

### Human Focus Areas
- **Architecture decisions** and system design
- **Product requirements** and UX design
- **Code review** and quality gates
- **Testing strategy** and deployment

### AI Focus Areas  
- **Boilerplate code** and repetitive tasks
- **Implementation** following established patterns
- **Unit test generation** and documentation
- **Code optimization** and refactoring

## Daily Development Workflow

### 1. Start Work Session
```bash
# Check current status
./scripts/github-automation/workflow-simple.sh status

# Triage any new issues
./scripts/github-automation/workflow-simple.sh triage
```

### 2. Select Work Type

**For Features:**
```bash
# Method 1: Use web interface (easiest)
gh issue create --web

# Method 2: CLI with template content  
gh issue create --title "[FEATURE] Your feature name" --body "$(cat .github/ISSUE_TEMPLATE/feature.md | tail -n +8)" --label "feature,needs-triage"

# Then run kickstart
./scripts/github-automation/feature-kickstart.sh [issue-number]
```

**For Quick Tasks:**
```bash
gh issue create --title "[QUICK] Your task" --body "$(cat .github/ISSUE_TEMPLATE/quick-task.md | tail -n +8)" --label "quick-task,needs-triage"
```

**For Bugs:**
```bash
gh issue create --title "[BUG] Bug description" --body "$(cat .github/ISSUE_TEMPLATE/bug.md | tail -n +8)" --label "bug,needs-triage"
```

### 3. Complete Work
```bash
# Commit with issue reference
git commit -m "feat: implement feature (fixes #123)"

# Close issue
gh issue close [number] --comment "Completed in commit [hash]"
```

## Git Workflow Integration

### Branch Naming Conventions
```bash
# Feature branches (new functionality)
feature/issue-number-short-description
# Example: feature/42-user-authentication

# Bug fix branches
fix/issue-number-bug-description
# Example: fix/38-login-error

# Quick task branches (<30 min work)
quick/issue-number-task-description
# Example: quick/45-update-readme

# Enhancement branches
enhance/issue-number-enhancement
# Example: enhance/50-improve-performance
```

### Commit Message Format
```bash
# Link commits to issues using keywords
git commit -m "feat: implement feature (fixes #123)"
git commit -m "fix: resolve bug (closes #456)"
git commit -m "docs: update readme (ref #789)"

# Keywords that close issues:
# - fixes, closes, resolves
# Keywords that reference issues:
# - ref, see, relates to
```

### Pull Request Workflow
```bash
# Create PR with issue reference
gh pr create --title "Feature: Description" \
  --body "Fixes #123

## Changes
- Implementation details
- Testing performed

## Memory-Bank Updates
- Updated relevant documentation"

# Link PR to project board automatically
# PR status updates issue status
```

## Best Practices

### Issue Creation
- **Use appropriate templates** for consistent structure
- **Check complexity boxes** for proper automation
- **Reference memory-bank** documentation when relevant
- **Include clear acceptance criteria**
- **Add to project board** automatically via scripts
- **Apply proper labels** for filtering and automation

### Development Process
- **One issue per task** - keep focused and actionable
- **Reference issue numbers** in all commits using keywords
- **Update labels** as work progresses through workflow
- **Close promptly** when work completes with summary comment
- **Link PRs to issues** using "fixes #123" in PR description
- **Update memory-bank** before closing implementation issues

### AI Collaboration
- **Let AI handle boilerplate** after human designs architecture
- **Use kickstart scripts** to eliminate setup overhead
- **Focus human time** on decisions and quality gates
- **Review AI work** for correctness and patterns
- **Document decisions** in memory-bank for future reference
- **Maintain test coverage** for all AI-generated code

### Code Review Standards
- **Verify tests pass** before requesting review
- **Check memory-bank alignment** with implementation
- **Review AI-generated code** for edge cases
- **Validate security practices** in all changes
- **Ensure documentation updates** accompany code changes

## Integration Points

### Memory Bank References
- Link issues to relevant `memory-bank/features/` documentation
- Update memory bank after significant implementation changes
- Use memory bank context for architectural decisions
- Reference [memory-bank-rules.md](./memory-bank-rules.md) for documentation standards
- Follow [documentation-framework.md](./documentation-framework.md) for file structure

### Project Configuration Integration
- Coding standards and quick rules
- Issue workflow reminders
- AI collaboration guidelines
- Tool-specific usage patterns

### Development Workflow Files
- **CLAUDE.md**: Quick command references and development workflows
- **startHere.md**: Project navigation and context
- **documentation-framework.md**: Documentation standards

## Workflow Optimization Tips

### For AI Assistants
1. **Always check for existing issues** before creating duplicates
2. **Reference memory-bank** for context before implementation
3. **Update documentation concurrently** with code changes
4. **Use automation scripts** for repetitive tasks
5. **Follow branch naming conventions** strictly
6. **Link all commits to issues** using keywords

### For Human Developers
1. **Review AI-generated PRs** for architectural alignment
2. **Use templates** for consistent issue creation
3. **Leverage automation** for project board management
4. **Focus on architecture** and let AI handle implementation
5. **Maintain memory-bank** as source of truth

### Common Pitfalls to Avoid
- **Skipping issue creation** for "quick" changes (always create issues)
- **Forgetting issue references** in commits (breaks automation)
- **Not updating labels** as work progresses (affects tracking)
- **Closing issues without summary** (loses context for future)
- **Bypassing branch workflow** (directly committing to main)

## Quick Reference Commands

### Issue Management
```bash
# List all open issues
gh issue list

# View specific issue
gh issue view [number]

# Create issue with template
gh issue create --web

# Close issue with comment
gh issue close [number] --comment "Summary"

# Update issue labels
gh issue edit [number] --add-label "in-progress"
```

### Project Board Management
```bash
# List project items
gh project list

# View project status
gh project view [project-number]

# Add issue to project (if automation fails)
gh project item-add [project-number] --owner [username] --url [issue-url]
```

### Branch and PR Management
```bash
# Create feature branch
git checkout -b feature/[issue-number]-[description]

# Push and create PR
git push -u origin feature/[issue-number]-[description]
gh pr create --title "Title" --body "Fixes #[number]"

# Check PR status
gh pr status

# Merge PR
gh pr merge [number] --squash
```

This workflow optimizes for rapid development while maintaining code quality through proper human-AI role separation, efficient automation, and comprehensive documentation practices.
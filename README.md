# Ask Randy 🤖

Slack-based Q&A system for content team to query Randy's Personal repo knowledge base with read-only MBIE access.

## What is This?

**Ask Randy** allows whitelisted content team members to ask questions about Randy's business philosophy, Anti-Rat Race principles, and client transformation methodologies via Slack - without direct access to the Personal repo.

**Key Features:**
- 💬 Natural language Q&A in Slack (#ask-randy channel)
- 🔍 MBIE semantic search across Personal repo memory-bank
- 🔒 Read-only enforcement (zero write access to Personal repo)
- 📚 Source citations for all answers
- 👥 Whitelist-based access control

## Quick Start

### For Content Team Members

1. **Join #ask-randy** Slack channel
2. **Ask questions** naturally:
   - "What common wisdom does Randy contradict?"
   - "How did Randy reduce Andrew's involvement by 90%?"
   - "What is the Portfolio CEO evolution strategy?"
3. **Receive AI-powered answers** with source citations from Randy's documentation

### For Setup/Administration

See `memory-bank/projectbrief.md` for complete project documentation.

**Requirements:**
- Slack workspace with claude-code-slack bot installed
- Whitelisted Slack user IDs in `.env`
- MBIE indexed Personal repo (already configured)

## Architecture

```
Slack (#ask-randy)
    ↓
Claude Code Slack Bot
    ↓
Ask-Randy Repo
    ├── tools/memory_rag/ (MBIE instance)
    │   └── Queries Personal/memory-bank/ (READ-ONLY)
    ├── CLAUDE.md (Read-only enforcement)
    └── .env (Whitelist configuration)
```

## Example Interaction

**User in #ask-randy:**
> "What common wisdom does Randy contradict?"

**Bot Response:**
```
Randy contradicts several pieces of common wisdom:

1. **"Work harder to succeed"**
   → Randy: Build systems that work while you sleep

2. **"Grow revenue first"**
   → Randy: Eliminate key-person risk first to create exit-ready assets

3. **"Scale through hiring"**
   → Randy: Scale through automation + delegation

Sources:
- Personal/memory-bank/strategy/personal-philosophy.md
- Personal/memory-bank/activeContext.md
```

## Documentation

- **Project Brief**: `memory-bank/projectbrief.md` - Goals, scope, success metrics
- **CLAUDE.md**: Read-only rules and MBIE query instructions
- **MBIE Configuration**: `tools/memory_rag/config.yml` - Semantic search tuning

## Security

**Read-Only Enforcement:**
- ❌ Cannot write to Personal repo files
- ❌ Cannot create issues in Personal repo
- ❌ Cannot execute git commands in Personal repo
- ✅ Can only query via MBIE semantic search

**Whitelist Control:**
- Only authorized content team members can access
- Managed via `.env` ALLOWED_USER_IDS
- Slack bot validates user permissions

## Technical Details

**Built With:**
- Template repo (memory-bank + MBIE infrastructure)
- MBIE 1.0.0 (semantic search engine)
- Claude Code Slack Bot integration
- ChromaDB vector database

**MBIE Configuration:**
- Indexes: Personal/memory-bank, docs/Team Lift LLC, strategy/
- Domains: anti_rat_race (2.5x boost), client_transformations (2.0x)
- Query latency: <500ms (p95)

## Links

- **GitHub Repository**: https://github.com/NoCapLife/ask-randy
- **GitHub Issue**: [#505 Ask Randy](https://github.com/NoCapLife/Personal/issues/505)
- **Personal Repo**: Not directly accessible (read-only via MBIE)
- **Memory-Bank Navigation**: `memory-bank/startHere.md`

---

**Status:** Active | **Owner:** Randy | **Created:** 2025-11-14

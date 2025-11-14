---
owner: Template Repository
last_updated: 2025-10-12
size: 🟢
status: production-ready
sources_of_truth: [README.md, technical-design.md]
related_files: [implementation.md, testing-strategy.md]
---

# MBIE: Memory-Bank Intelligence Engine

**Purpose:** Semantic search and intelligent documentation retrieval system
**Status:** Production Ready (v1.0.0)
**Type:** Reusable Tool / Infrastructure Component

## Overview

MBIE (Memory-Bank Intelligence Engine) is a self-contained semantic search system that enables AI-powered documentation retrieval with priority scoring, temporal context awareness, and adaptive learning capabilities.

## Current Status

- ✅ **Extraction Complete**: Successfully extracted and sanitized from Personal repo
- ✅ **Dependencies Resolved**: All Python dependency conflicts fixed
- ✅ **Tests Functional**: ~60% test suite passing (core functionality validated)
- ✅ **CI/CD Configured**: GitHub Actions workflow operational
- 📦 **Location**: `tools/memory_rag/`

## Quick Navigation

### Core Documentation Files

- **[requirements.md](./requirements.md)** 🟢 - What MBIE accomplishes and why
- **[technical-design.md](./technical-design.md)** 🟡 - Architecture and how it works internally
- **[implementation.md](./implementation.md)** 🟡 - Development guide and file structure
- **[testing-strategy.md](./testing-strategy.md)** 🟢 - Test approach and validation

### Implementation Location

- **Source Code**: `tools/memory_rag/`
- **Core Modules**: `tools/memory_rag/core/`
- **CLI Interface**: `tools/memory_rag/cli.py`
- **Tests**: `tools/memory_rag/tests/`
- **Configuration**: `tools/memory_rag/config.yml.template`

## Key Capabilities

1. **Semantic Search**: Natural language understanding via sentence transformers
2. **Priority Scoring**: Intelligent relevance ranking with configurable boosts
3. **Status Awareness**: Filter by document status (completed, in-progress, pending)
4. **Temporal Context**: Time-aware search for current/urgent items
5. **Multi-Domain Support**: Customizable knowledge domains with boost factors
6. **Adaptive Learning**: Self-improving intelligence based on usage patterns

## Quick Start

```bash
cd tools/memory_rag
python3 -m venv mbie_env
source mbie_env/bin/activate
pip install -r requirements_latest_stable.txt
python cli.py quickstart
```

## Navigation Tips

- **New to MBIE?** Start with [requirements.md](./requirements.md)
- **Understanding architecture?** Read [technical-design.md](./technical-design.md) → `## System Architecture`
- **Implementing MBIE?** Follow [implementation.md](./implementation.md) → `## Installation Steps`
- **Testing MBIE?** Review [testing-strategy.md](./testing-strategy.md)

## File Size Guide

- **README.md** (this file): 🟢 75 lines
- **requirements.md**: 🟢 ~200 lines
- **technical-design.md**: 🟡 ~450 lines
- **implementation.md**: 🟡 ~400 lines
- **testing-strategy.md**: 🟢 ~250 lines

---

**Related Context**: See `tools/memory_rag/README.md` for user-facing installation guide

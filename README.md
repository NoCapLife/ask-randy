# Project Template with Memory-Bank & MBIE

A professional-grade project template featuring a comprehensive AI-optimized documentation system (Memory-Bank) and an intelligent semantic search tool (MBIE - Memory-Bank Intelligence Engine).

## What is This Template?

This repository provides two powerful components for AI-assisted project development:

1. **Memory-Bank Documentation Framework** - A modular documentation system designed for optimal AI navigation and human understanding
2. **MBIE Tool** - A production-ready semantic search engine for intelligent documentation retrieval

## Quick Start

### Option 1: Use as GitHub Template

1. Click "Use this template" button on GitHub
2. Create your new repository
3. Clone your new repository
4. Follow the customization steps below

### Option 2: Clone Directly

```bash
git clone https://github.com/[your-org]/Template.git my-new-project
cd my-new-project
rm -rf .git
git init
```

## Customizing for Your Project

### Step 1: Update Core Documentation

Edit these files with your project information:

- **`memory-bank/projectbrief.md`** - Replace `[Project Name]`, `[Project Owner]`, goals, scope
- **`memory-bank/executiveSummary.md`** - Update project overview, status, team info
- **`memory-bank/activeContext.md`** - Set current focus, milestones, priorities
- **`memory-bank/ceo-dashboard.md`** - Configure real-time status tracking
- **`memory-bank/techContext.md`** - Define your technology stack
- **`memory-bank/productContext.md`** - Describe your product vision

### Step 2: Choose Project Structure

Select the appropriate project organization pattern based on complexity:

**Standard Structure** (Most Projects):
```bash
# Copy template for client delivery, features, operational projects
cp -r memory-bank/projects/example-templates/standard-project/ memory-bank/projects/[project-name]/
# Edit README.md, context.md, CHANGELOG.md with your details
```

**Enhanced Structure** (Complex Multi-Phase Projects):
```bash
# Copy template for partnerships, acquisitions, strategic initiatives (20K+ words)
cp -r memory-bank/projects/example-templates/enhanced-project/ memory-bank/projects/[project-name]/
# Add strategy documents to strategy/
# Add expert analyses to analysis/
# Add coordination materials to coordination/
```

See **`memory-bank/projects/README.md`** for complete decision criteria and file placement guidelines.

### Step 3: Navigation Hub

The **`memory-bank/startHere.md`** file is your master navigation hub. Review and customize:
- Task-specific navigation paths
- File relationships
- Quick reference links

### Step 4: Feature Documentation

The template includes three complete feature examples:
- **`features/example-calculator/`** - Simple feature pattern (~4-6 hours)
- **`features/example-dashboard/`** - Complex feature pattern (~4-6 weeks)
- **`features/example-api-integration/`** - Integration pattern (~2-3 weeks)

For each new feature, use the 8-file modular structure:
1. `README.md` - Navigation hub
2. `requirements.md` - Capabilities and user stories
3. `user-experience.md` - UI/UX design
4. `technical-design.md` - Architecture and implementation
5. `implementation.md` - Code guide and development
6. `content-strategy.md` - Messaging and copy
7. `testing-strategy.md` - Test coverage
8. `decisions.md` - Design decisions and rationale

### Step 5: MBIE Integration (Optional)

To enable intelligent semantic search of your documentation:

```bash
cd tools/memory_rag

# Install dependencies
pip install -r requirements.txt

# Or install as package
pip install -e .

# Index your documentation
python -m memory_rag.cli index

# Search your docs
python -m memory_rag.cli search "how do I implement authentication?"
```

See **`tools/memory_rag/README.md`** for complete MBIE documentation.

## What's Included

### Memory-Bank Documentation System

```
memory-bank/
├── startHere.md              # Master navigation hub
├── ceo-dashboard.md          # Real-time operational view
├── activeContext.md          # Strategic context and priorities
├── projectbrief.md           # Core project definition
├── executiveSummary.md       # High-level overview
├── techContext.md            # Technology stack
├── systemPatterns.md         # Architecture patterns
├── progress.md               # Implementation status
├── projects/                 # Project organization patterns & templates
│   ├── README.md            # Standard vs Enhanced structures guide
│   └── example-templates/
│       ├── standard-project/     # Client delivery, features, operational
│       └── enhanced-project/     # Multi-phase, partnerships, strategic
│           ├── strategy/         # Planning documents (what to do)
│           ├── analysis/         # Validation documents (why it works)
│           └── coordination/     # Tracking documents (how to execute)
├── guides/                   # Framework and workflow guides
│   ├── documentation-framework.md (includes Part III: Project Patterns)
│   ├── memory-bank-rules.md
│   ├── ai-integration-guide.md
│   └── subagent-collaboration-guide.md
└── features/                 # Feature documentation
    ├── example-calculator/
    ├── example-dashboard/
    ├── example-api-integration/
    └── mbie/                 # MBIE documentation
```

### MBIE Tool (Memory-Bank Intelligence Engine)

```
tools/memory_rag/
├── cli.py                    # Command-line interface
├── core/                     # Core functionality
│   ├── chunker.py           # Document processing
│   ├── embedder.py          # Semantic embeddings
│   ├── indexer.py           # Index management
│   ├── searcher.py          # Semantic search
│   ├── analytics.py         # Usage tracking
│   └── learning.py          # Adaptive learning
├── tests/                    # Comprehensive test suite
├── config.yml               # Configuration
└── README.md                # MBIE documentation
```

### Development Infrastructure

- **`CLAUDE.md`** - Comprehensive Claude Code development workflows
- **`.claude/commands/`** - Custom Claude slash commands
  - `/memory-bank` - Memory-bank navigation assistant
  - `/pr-review` - Pull request review guide
- **`.github/workflows/`** - CI/CD pipeline for MBIE
- **`.gitignore`** - Pre-configured exclusions

## File Size Guide (AI Context Optimization)

The memory-bank uses a color-coded system for AI context optimization:

- 🟢 **AI-Friendly** (<400 lines) - Use directly in AI context
- 🟡 **Large** (400-600 lines) - Use section-based navigation
- 🔴 **Very Large** (>600 lines) - Always use executive summaries

See **`memory-bank/guides/executive-summaries.md`** for navigation patterns.

## Key Features

### Memory-Bank Documentation Framework

- **AI-Optimized Navigation** - File size categorization and strategic navigation paths
- **Modular Feature Structure** - Consistent 8-file pattern for all features
- **Dual-Context System** - Operational (`ceo-dashboard.md`) + Strategic (`activeContext.md`)
- **Multi-Agent Support** - Built-in coordination patterns for AI collaboration
- **Template Examples** - Three complete feature examples to learn from

### MBIE Intelligence Engine

- **Semantic Search** - Find documentation by meaning, not just keywords
- **Adaptive Learning** - Improves results based on usage patterns
- **Priority Scoring** - Intelligent ranking of search results
- **Calendar Integration** - Context-aware search with time awareness
- **Comprehensive Testing** - 60+ tests with 85%+ coverage
- **CI/CD Pipeline** - Automated testing, linting, security scanning

## Documentation Guides

Essential guides for using this template:

- **`memory-bank/AI_GUIDE.md`** - Efficient AI assistant usage patterns
- **`memory-bank/guides/documentation-framework.md`** - Complete documentation structure
- **`memory-bank/guides/memory-bank-rules.md`** - Update protocols and workflows
- **`memory-bank/guides/ai-integration-guide.md`** - AI tool integration patterns
- **`memory-bank/guides/subagent-collaboration-guide.md`** - Multi-agent coordination
- **`CLAUDE.md`** - Claude Code development workflows

## Development Workflow

### Git Workflow (From CLAUDE.md)

1. **Check compliance** - Never commit to main
2. **Create feature branch** - `feature/issue-number-description`
3. **Work → Test → Security → Commit**
4. **Push and create PR**

### Memory-Bank Updates

Follow the **Dual-Update Rule**:
- **Operational changes** → Update `ceo-dashboard.md`
- **Strategic changes** → Update `activeContext.md`
- Keep both files synchronized

See **`memory-bank/guides/memory-bank-rules.md`** for complete update protocols.

## Quality Validation

This toolkit is validated through real client deployments and local testing, not CI/CD pipelines.

### Pre-Deployment Validation

Before deploying to a client environment, run the validation script:

```bash
./scripts/validate-before-deployment.sh
```

This script validates:
- **Python version** - Ensures Python 3.9+ is available
- **MBIE dependencies** - Installs and verifies required packages
- **MBIE test suite** - Runs comprehensive test coverage
- **MBIE CLI** - Confirms command-line interface works
- **Placeholder detection** - Identifies values needing customization

### Why No CI?

This repository serves as a **consulting deployment toolkit**, not a continuously developed product. Real validation happens through:

1. **Local testing** before client deployment
2. **Client environment validation** during deployment
3. **Real-world usage** in production client systems

Empirical evidence (successful SleekAI deployment) proves CI is unnecessary overhead for this use case.

## Technology Stack

### Memory-Bank
- Markdown-based documentation
- AI-optimized structure
- GitHub integration

### MBIE Tool
- **Language**: Python 3.9+
- **Embeddings**: sentence-transformers
- **Vector Search**: FAISS
- **NLP**: spaCy, scikit-learn
- **Testing**: pytest, pytest-cov
- **Quality**: black, flake8, mypy, bandit

## Contributing

This is a template repository. For your own projects:

1. Customize the template for your needs
2. Follow the memory-bank update rules
3. Maintain the modular structure
4. Use MBIE for intelligent documentation search

## License

[Specify your license here]

## Support & Resources

- **Full Documentation**: Start at `memory-bank/startHere.md`
- **MBIE Guide**: See `tools/memory_rag/README.md`
- **Development Workflows**: See `CLAUDE.md`
- **Feature Examples**: Explore `memory-bank/features/example-*/`

## Project Status

**Template Version**: 1.0
**Memory-Bank Files**: 78 markdown files
**MBIE Tool**: Production-ready (45 Python files, 15+ tests)
**Maintenance**: Active

---

**Getting Started**: Read `memory-bank/startHere.md` for complete navigation
**AI Assistants**: Start with `memory-bank/AI_GUIDE.md` for optimization patterns
**Developers**: Review `CLAUDE.md` for development workflows

---
owner: Template Repository
last_updated: 2025-10-12
size: 🟡
status: production-ready
sources_of_truth: [implementation.md]
related_files: [technical-design.md, testing-strategy.md]
---

# MBIE Implementation Guide

## Executive Summary

MBIE is implemented as a self-contained Python tool in `tools/memory_rag/`. Installation requires Python 3.9-3.11, creating a virtual environment, installing pinned dependencies from `requirements_latest_stable.txt`, and configuring via `config.yml`. Core workflow: (1) Copy `tools/memory_rag/` to target repo, (2) Setup venv and install deps, (3) Configure `config.yml` from template, (4) Run `python cli.py index --full`, (5) Query via `python cli.py query "search term"`. Key files: `core/chunker.py` (document parsing), `core/embedder.py` (embeddings), `core/searcher.py` (hybrid search), `core/intelligence.py` (status/priority scoring), `cli.py` (command interface).

## Installation Steps

### Step 1: Prerequisites Check

```bash
# Verify Python version (3.9, 3.10, or 3.11 required)
python3 --version

# Should output: Python 3.9.x, 3.10.x, or 3.11.x
```

### Step 2: Copy MBIE to Target Repository

```bash
# From Template repository
cd /path/to/Template
cp -r tools/memory_rag /path/to/target-repo/tools/

# Verify copy
ls /path/to/target-repo/tools/memory_rag/
# Should see: cli.py, core/, tests/, config.yml.template, requirements_latest_stable.txt
```

### Step 3: Create Virtual Environment

```bash
cd /path/to/target-repo/tools/memory_rag

# Create virtual environment
python3 -m venv mbie_env

# Activate (macOS/Linux)
source mbie_env/bin/activate

# Activate (Windows)
mbie_env\Scripts\activate

# Verify activation
which python
# Should point to: .../memory_rag/mbie_env/bin/python
```

### Step 4: Install Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install pinned dependencies (CRITICAL: use pinned versions)
pip install -r requirements_latest_stable.txt

# Verify installation
python -c "import sentence_transformers; print('✅ Dependencies installed')"
```

**Dependency Version Note:**
MBIE uses pinned versions to avoid dependency conflicts:
- `sentence-transformers==2.7.0` (last stable before 3.x breaking changes)
- `transformers==4.34.0` (required by sentence-transformers 2.7.0)
- `huggingface_hub==0.16.4` (non-yanked stable version)
- `tokenizers==0.14.0` (required by transformers 4.34.0)
- `chromadb==0.4.22` (stable without 0.5.x conflicts)

### Step 5: Configuration

```bash
# Copy configuration template
cp config.yml.template config.yml

# Edit configuration for your project
nano config.yml  # or vim/code/etc
```

**Minimal Configuration:**
```yaml
model:
  name: sentence-transformers/all-MiniLM-L6-v2
  device: cpu
  batch_size: 32

storage:
  memory_bank_root: ../../memory-bank  # Adjust path to your memory-bank
  index_path: ./index
  cache_path: ./cache

chunking:
  small_file_lines: 400
  medium_file_lines: 600
  chunk_size: 512
  chunk_overlap: 50

search:
  top_k: 10
  relevance_threshold: 0.7
  hybrid_alpha: 0.7

domains: {}  # Add custom domains as needed
```

### Step 6: Initial Index

```bash
# Run full index (first time)
python cli.py index --config config.yml --full

# Expected output:
# 🔍 Scanning memory bank...
# 📄 Found 150 markdown files
# 🧩 Chunking documents...
# 🎯 Generated 450 chunks
# 💾 Storing in ChromaDB...
# ✅ Successfully indexed 150 documents in 2.5 minutes
```

### Step 7: Test Query

```bash
# Test semantic search
python cli.py query "current week objectives" --config config.yml

# Expected output:
# 🔍 Searching for: "current week objectives"
#
# 📄 activeContext.md → ## Current Focus (Score: 0.92)
#    This week's focus is on completing the authentication flow...
#
# 📄 progress.md → ## Week 3 Status (Score: 0.87)
#    Week 3 objectives include database migration and...
```

## File Structure

### Project Layout

```
tools/memory_rag/
├── cli.py                              # CLI entry point (400 lines)
├── config.yml                          # User configuration (generated)
├── config.yml.template                 # Configuration template
├── requirements_latest_stable.txt      # Pinned dependencies
├── setup.py                            # Package installation config
├── README.md                           # User-facing documentation
│
├── core/                               # Core modules
│   ├── __init__.py                     # Module exports
│   ├── chunker.py                      # Document chunking (350 lines)
│   ├── embedder.py                     # Embedding generation (200 lines)
│   ├── searcher.py                     # Hybrid search (400 lines)
│   ├── indexer.py                      # Index management (350 lines)
│   ├── intelligence.py                 # Intelligence processing (1800 lines)
│   ├── learning.py                     # Adaptive learning (800 lines)
│   └── analytics.py                    # Usage analytics (700 lines)
│
├── tests/                              # Test suite
│   ├── test_chunker.py                 # Chunking tests (400 lines)
│   ├── test_embedder.py                # Embedding tests (300 lines)
│   ├── test_intelligence.py            # Intelligence tests (440 lines)
│   ├── test_integration.py             # Integration tests (250 lines)
│   ├── test_performance.py             # Performance tests (200 lines)
│   ├── test_cli.py                     # CLI tests (370 lines)
│   └── test_error_handling.py          # Error handling tests (340 lines)
│
├── index/                              # ChromaDB storage (generated)
├── cache/                              # Embedding cache (generated)
├── mbie_env/                           # Virtual environment (generated)
└── logs/                               # Application logs (generated)
```

### Key Files Explained

**cli.py** (400 lines)
- Command-line interface using Click framework
- Commands: `index`, `query`, `stats`, `backup`, `restore`, `evaluate`
- Configuration loading and validation
- Result formatting and output

**core/chunker.py** (350 lines)
- `MemoryBankChunker` class
- Markdown parsing and section extraction
- File size categorization (🟢🟡🔴)
- Navigation breadcrumb generation
- Executive summary extraction

**core/embedder.py** (200 lines)
- `LocalEmbedder` class
- Sentence transformer model loading
- Embedding generation (384-dim vectors)
- MD5-based caching system
- Batch processing optimization

**core/searcher.py** (400 lines)
- `HybridSearcher` class
- ChromaDB collection management
- Semantic similarity search
- BM25 keyword search
- Hybrid scoring and ranking

**core/indexer.py** (350 lines)
- `IncrementalIndexer` class
- File system scanning
- Modification tracking
- Coordinated indexing workflow
- Incremental update logic

**core/intelligence.py** (1800 lines)
- `IntelligenceProcessor` class
- `SemanticStatusParser` - Status detection
- `TemporalContextExtractor` - Time awareness
- `PriorityScoringEngine` - Priority calculation
- Boost cap enforcement

## API Reference

### Python API Usage

#### Basic Query Example

```python
from tools.memory_rag.core import HybridSearcher, LocalEmbedder, IncrementalIndexer
import yaml

# Load configuration
with open('tools/memory_rag/config.yml') as f:
    config = yaml.safe_load(f)

# Initialize components
embedder = LocalEmbedder(config)
searcher = HybridSearcher(config, embedder)
indexer = IncrementalIndexer(config)

# Ensure index exists
if not searcher.collection_exists():
    print("Index not found. Creating...")
    indexer.full_index()

# Perform query
results = searcher.search(
    query="authentication flow",
    top_k=5,
    domain=None,
    status_filter=None
)

# Process results
for i, result in enumerate(results, 1):
    print(f"\n{i}. {result.chunk.navigation_path}")
    print(f"   Score: {result.combined_score:.2f}")
    print(f"   Preview: {result.chunk.content[:100]}...")
```

#### Advanced Query with Filters

```python
# Query with status filter
results = searcher.search(
    query="database schema",
    top_k=10,
    domain="technical",
    status_filter="in_progress"
)

# Query for current/urgent items only
results_urgent = searcher.search(
    query="sprint deliverables",
    current_only=True,
    urgent_only=True
)

# Domain-specific query
results_business = searcher.search(
    query="revenue optimization",
    domain="business"
)
```

#### Indexing Operations

```python
from tools.memory_rag.core import IncrementalIndexer

indexer = IncrementalIndexer(config)

# Full reindex (clears existing index)
doc_count = indexer.full_index()
print(f"Indexed {doc_count} documents")

# Incremental update (only changed files)
updated = indexer.incremental_index()
print(f"Updated {updated['added']} added, {updated['modified']} modified")

# Get index statistics
stats = indexer.get_statistics()
print(f"Total chunks: {stats['total_chunks']}")
print(f"Last updated: {stats['last_updated']}")
```

### CLI Reference

#### Index Commands

```bash
# Full reindex (delete existing index)
python cli.py index --config config.yml --full

# Incremental index (update only changed files)
python cli.py index --config config.yml --incremental

# Force reindex specific directory
python cli.py index --config config.yml --full --path memory-bank/features/
```

#### Query Commands

```bash
# Basic query
python cli.py query "search term"

# Query with config file
python cli.py query "search term" --config custom_config.yml

# Query with filters
python cli.py query "authentication" --status in_progress --domain technical

# Query for current items
python cli.py query "objectives" --current-only

# Query for urgent items
python cli.py query "deliverables" --urgent-only

# Limit results
python cli.py query "api endpoints" --limit 5
```

#### Management Commands

```bash
# View statistics
python cli.py stats --config config.yml

# Backup index
python cli.py backup --output mbie_backup_2025-10-12.zip

# Restore index
python cli.py restore --input mbie_backup_2025-10-12.zip

# Evaluate search quality
python cli.py evaluate --config config.yml
```

## Configuration Guide

### Configuration Options

#### Model Configuration

```yaml
model:
  name: sentence-transformers/all-MiniLM-L6-v2  # Embedding model
  device: cpu                                    # 'cpu' or 'cuda'
  batch_size: 32                                 # Embedding batch size
```

**Supported Models:**
- `all-MiniLM-L6-v2` (default): 384-dim, fast, good quality
- `all-mpnet-base-v2`: 768-dim, slower, better quality
- `multi-qa-mpnet-base-dot-v1`: 768-dim, optimized for Q&A

#### Storage Configuration

```yaml
storage:
  memory_bank_root: ../../memory-bank           # Path to documentation root
  index_path: ./index                           # ChromaDB storage location
  cache_path: ./cache                           # Embedding cache directory
  additional_sources:                           # Extra directories to index
    - ../../docs/
    - ../../wiki/
```

#### Chunking Configuration

```yaml
chunking:
  small_file_lines: 400                         # 🟢 threshold
  medium_file_lines: 600                        # 🟡 threshold
  chunk_size: 512                               # Max tokens per chunk
  chunk_overlap: 50                             # Overlap between chunks
  section_regex: '^##\s+'                       # Section header pattern
```

#### Search Configuration

```yaml
search:
  top_k: 10                                     # Max results returned
  relevance_threshold: 0.7                      # Min score (0-1)
  hybrid_alpha: 0.7                             # Semantic weight (0-1)
                                                # 1.0 = pure semantic
                                                # 0.0 = pure keyword
```

#### Domain Configuration

```yaml
domains:
  current_work:
    boost: 2.0                                  # Result score multiplier
    keywords:                                   # Boost trigger keywords
      - urgent
      - priority
      - critical
    files:                                      # Glob patterns to match
      - 'activeContext.md'
      - 'current*.md'
      - 'features/*/progress.md'

  business:
    boost: 1.5
    keywords:
      - revenue
      - client
      - strategic
    files:
      - 'business/*.md'
      - 'clients/*.md'
```

#### Intelligence Configuration

```yaml
intelligence:
  enabled: true                                 # Enable intelligence layer
  boost_cap: 3.0                                # Max combined boost

  status_parsing:
    checkbox_patterns:
      completed: ['\[x\]', '\[X\]']
      pending: ['\[ \]']
      in_progress: ['\[-\]', '\[~\]']
    progress_keywords:
      completed: [COMPLETED, DONE, ✅, FINISHED]
      in_progress: [IN PROGRESS, CURRENT, 🔄, WORKING]
      pending: [PENDING, TODO, 📋, UPCOMING]

  temporal_context:
    business_phases:
      current_quarter: Q3 2025
      current_week: Week 3
      current_phase: Pre-Sprint Preparation
    critical_dates:
      sprint_start: 2025-08-20
      sprint_end: 2025-08-22
    relevance_decay:
      current: 1.0
      upcoming: 0.8
      recent: 0.6
      historical: 0.3

  priority_scoring:
    keyword_multipliers:
      PRIMARY FOCUS: 2.0
      CRITICAL: 1.8
      HIGH PRIORITY: 1.5
      URGENT: 1.4
    hierarchy_boosts:
      strategic: 1.3
      tactical: 1.1
      operational: 1.0
```

## Development Guide

### Adding New Features

#### Step 1: Plan Feature
1. Document in `memory-bank/features/mbie/`
2. Update `technical-design.md` with architecture changes
3. Update `implementation.md` with development steps

#### Step 2: Implement Core Logic
```python
# Example: Adding a new intelligence processor
# File: core/intelligence.py

class NewIntelligenceProcessor:
    """Process a new type of intelligence signal"""

    def __init__(self, config: dict):
        self.config = config
        self.enabled = config.get('new_intelligence', {}).get('enabled', False)

    def process(self, content: str, metadata: dict) -> float:
        """Return boost factor (1.0-3.0)"""
        if not self.enabled:
            return 1.0

        # Implementation logic here
        boost = 1.0
        # ... calculation ...
        return min(boost, 3.0)
```

#### Step 3: Integrate with IntelligenceProcessor
```python
# Update IntelligenceProcessor class
def process_chunk_intelligence(self, content: str, doc_path: str) -> IntelligenceMetadata:
    # Existing processors
    status_info = self.status_parser.parse_chunk_status(content)
    temporal_context = self.temporal_extractor.extract_temporal_context(content, doc_path)
    priority_markers = self.priority_engine.extract_priority_markers(content, doc_path)

    # Add new processor
    new_boost = self.new_processor.process(content, {'path': doc_path})

    # Combine boosts
    overall_boost = (
        status_boost *
        temporal_boost *
        priority_boost *
        new_boost  # Add new boost
    )

    # Cap at maximum
    overall_boost = min(overall_boost, self.boost_cap)

    return IntelligenceMetadata(...)
```

#### Step 4: Add Configuration
```yaml
# config.yml.template
intelligence:
  new_intelligence:
    enabled: true
    threshold: 0.5
    keywords:
      - important_keyword
```

#### Step 5: Write Tests
```python
# tests/test_intelligence.py

def test_new_intelligence_processor():
    """Test new intelligence processor"""
    config = {
        'new_intelligence': {
            'enabled': True,
            'threshold': 0.5
        }
    }

    processor = NewIntelligenceProcessor(config)
    boost = processor.process("content with important_keyword", {})

    assert boost > 1.0
    assert boost <= 3.0
```

#### Step 6: Update Documentation
- Update `technical-design.md` → ## Component Architecture
- Update `implementation.md` → ## API Reference
- Update `README.md` in `tools/memory_rag/`

### Running Tests

```bash
# Activate virtual environment
source mbie_env/bin/activate

# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_intelligence.py -v

# Run with coverage
pytest tests/ --cov=core --cov-report=term

# Run performance tests
pytest tests/test_performance.py -v
```

### Debugging Tips

**Enable Debug Logging:**
```python
# In cli.py or your script
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Inspect Embeddings:**
```python
from core.embedder import LocalEmbedder
embedder = LocalEmbedder(config)

# Generate test embedding
text = "sample text for testing"
embedding = embedder.embed_query(text)
print(f"Embedding dimension: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
```

**Check ChromaDB Contents:**
```python
from core.searcher import HybridSearcher
searcher = HybridSearcher(config, embedder)

# Get collection info
collection = searcher.collection
print(f"Total documents: {collection.count()}")

# Sample results
results = collection.peek(limit=5)
print(results)
```

## Troubleshooting

### Common Issues

**Issue: Import errors when running tests**
```bash
# Fix: Ensure tests use relative imports
# Bad:  from tools.memory_rag.core.chunker import ...
# Good: from core.chunker import ...
```

**Issue: Dependency conflicts during installation**
```bash
# Fix: Use pinned versions from requirements_latest_stable.txt
pip install -r requirements_latest_stable.txt

# If still issues, create fresh venv
deactivate
rm -rf mbie_env
python3 -m venv mbie_env
source mbie_env/bin/activate
pip install -r requirements_latest_stable.txt
```

**Issue: ChromaDB errors on first run**
```bash
# Fix: Ensure index directory has write permissions
chmod -R 755 index/

# Or specify different path in config.yml
storage:
  index_path: ~/mbie_index
```

**Issue: Model download fails**
```bash
# Fix: Check internet connection and HuggingFace access
python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('all-MiniLM-L6-v2'); print('OK')"

# If behind proxy, set environment variables
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
```

---

**Next Steps**: See [testing-strategy.md](./testing-strategy.md) for testing approach

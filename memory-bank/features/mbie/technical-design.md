---
owner: Template Repository
last_updated: 2025-10-12
size: 🟡
status: production-ready
sources_of_truth: [technical-design.md]
related_files: [implementation.md, requirements.md]
---

# MBIE Technical Design & Architecture

## Executive Summary

MBIE uses a **hybrid semantic + keyword search architecture** built on sentence transformers and ChromaDB. The system consists of four layers: (1) Document chunking and preprocessing, (2) Semantic embedding generation, (3) Vector storage and hybrid search, (4) Intelligence processing (status, temporal, priority scoring). Core workflow: Index phase chunks documents → embeds content → stores in ChromaDB; Query phase embeds query → hybrid search → applies intelligence boosts → returns ranked results.

## System Architecture

### High-Level Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        CLI Layer                             │
│                      (cli.py)                                │
│  Commands: index, query, stats, backup, restore             │
└──────────────┬──────────────────────────────────────────────┘
               │
         ┌─────▼─────────────────────────────────────────┐
         │         Core Processing Layer                  │
         ├────────────────────────────────────────────────┤
         │  ┌──────────────────────────────────────────┐ │
         │  │  IncrementalIndexer                      │ │
         │  │  - Manages index lifecycle               │ │
         │  │  - Coordinates chunking, embedding       │ │
         │  └──────────────────────────────────────────┘ │
         │                                                │
         │  ┌──────────────────────────────────────────┐ │
         │  │  MemoryBankChunker                       │ │
         │  │  - Parses markdown documents             │ │
         │  │  - Creates semantic chunks               │ │
         │  └──────────────────────────────────────────┘ │
         │                                                │
         │  ┌──────────────────────────────────────────┐ │
         │  │  LocalEmbedder                           │ │
         │  │  - Generates embeddings (384-dim)        │ │
         │  │  - Caches computed embeddings            │ │
         │  └──────────────────────────────────────────┘ │
         │                                                │
         │  ┌──────────────────────────────────────────┐ │
         │  │  HybridSearcher                          │ │
         │  │  - Semantic + keyword search             │ │
         │  │  - Ranking and filtering                 │ │
         │  └──────────────────────────────────────────┘ │
         │                                                │
         │  ┌──────────────────────────────────────────┐ │
         │  │  IntelligenceProcessor                   │ │
         │  │  - Status parsing                        │ │
         │  │  - Temporal context                      │ │
         │  │  - Priority scoring                      │ │
         │  └──────────────────────────────────────────┘ │
         └────────────────────────────────────────────────┘
                              │
         ┌────────────────────▼───────────────────────────┐
         │           Storage Layer                        │
         ├────────────────────────────────────────────────┤
         │  ChromaDB (Vector Database)                    │
         │  - Stores embeddings + metadata                │
         │  - Performs similarity search                  │
         │  - Persistent local storage                    │
         └────────────────────────────────────────────────┘
```

## Data Models & Types

### Core Data Structures

#### Chunk (Document Fragment)
```python
@dataclass
class Chunk:
    chunk_id: str                # Unique identifier (MD5 hash)
    document_path: str           # Relative path from memory-bank root
    section_header: str          # Markdown section title
    content: str                 # Actual text content
    navigation_path: str         # Breadcrumb (file.md → Section → Subsection)
    start_line: int              # Line number where chunk starts
    end_line: int                # Line number where chunk ends
    metadata: Dict[str, Any]     # Additional metadata (size category, etc.)
```

#### SearchResult (Query Response)
```python
@dataclass
class SearchResult:
    chunk: Chunk                 # The matched document fragment
    semantic_score: float        # Cosine similarity score (0-1)
    keyword_score: float         # BM25 keyword match score (0-1)
    combined_score: float        # Weighted hybrid score
    domain_boost: float          # Applied domain multiplier (1.0+)
    intelligence_boost: float    # Applied intelligence multiplier (1.0-3.0)
    status_info: StatusInfo      # Parsed status information
    temporal_context: TemporalContext  # Time-awareness metadata
```

#### StatusInfo (Document Status)
```python
@dataclass
class StatusInfo:
    status_type: StatusType      # COMPLETED | IN_PROGRESS | PENDING | UNKNOWN
    confidence: float            # Confidence score (0-1)
    completion_percentage: float # Percentage of completed items
    checkbox_indicators: List[CheckboxInfo]  # Parsed checkboxes
    progress_markers: List[str]  # Found keywords
```

#### TemporalContext (Time Awareness)
```python
@dataclass
class TemporalContext:
    current_relevance: float     # How relevant to current time (0-1)
    urgency_score: float         # Deadline urgency (0-1)
    time_markers: List[TimeMarker]  # Detected dates/phases
    business_phase: str          # Current quarter/week/phase
```

### Configuration Schema

```yaml
# config.yml structure
model:
  name: sentence-transformers/all-MiniLM-L6-v2  # Embedding model
  device: cpu | cuda                            # Compute device
  batch_size: 32                                # Embedding batch size

storage:
  memory_bank_root: ./memory-bank               # Documentation root
  index_path: ./index                           # ChromaDB storage
  cache_path: ./cache                           # Embedding cache
  additional_sources: []                        # Extra directories

chunking:
  small_file_lines: 400                         # Threshold for small files
  medium_file_lines: 600                        # Threshold for medium files
  chunk_size: 512                               # Max tokens per chunk
  chunk_overlap: 50                             # Overlap between chunks
  section_regex: '^##\s+'                       # Section header pattern

search:
  top_k: 10                                     # Max results returned
  relevance_threshold: 0.7                      # Min score threshold
  hybrid_alpha: 0.7                             # Semantic weight (0-1)

domains:
  current_work:
    boost: 2.0                                  # Result multiplier
    keywords: [urgent, priority, critical]      # Boost keywords
    files: ['current*.md', 'active*.md']        # Glob patterns

intelligence:
  enabled: true                                 # Enable intelligence layer
  boost_cap: 3.0                                # Max combined boost
  status_parsing:
    checkbox_patterns:
      completed: ['\[x\]', '\[X\]']
      pending: ['\[ \]']
      in_progress: ['\[-\]', '\[~\]']
    progress_keywords:
      completed: [COMPLETED, DONE, ✅]
      in_progress: [IN PROGRESS, CURRENT, 🔄]
      pending: [PENDING, TODO, 📋]
  temporal_context:
    business_phases:
      current_quarter: Q3 2025
      current_week: Week 3
    critical_dates:
      sprint_start: 2025-08-20
  priority_scoring:
    keyword_multipliers:
      PRIMARY FOCUS: 2.0
      CRITICAL: 1.8
```

## Business Logic Engine

### Indexing Workflow

```
1. Scan Memory Bank
   ├─ Walk directory tree from memory_bank_root
   ├─ Filter *.md files
   └─ Track file modification times

2. Chunk Documents
   ├─ Parse markdown structure
   ├─ Categorize by file size (🟢🟡🔴)
   ├─ Extract executive summaries (if present)
   ├─ Split large sections into semantic chunks
   └─ Preserve navigation breadcrumbs

3. Generate Embeddings
   ├─ Check embedding cache (MD5 hash)
   ├─ Batch process uncached chunks (size=32)
   ├─ Generate 384-dim vectors (sentence transformers)
   └─ Cache embeddings for reuse

4. Store in ChromaDB
   ├─ Create/update vector collection
   ├─ Store embeddings + full metadata
   ├─ Build BM25 keyword index
   └─ Persist to disk
```

### Query Workflow

```
1. Process Query
   ├─ Normalize text (lowercase, trim)
   ├─ Generate query embedding (384-dim)
   └─ Extract query intent keywords

2. Hybrid Search
   ├─ Semantic Search:
   │  ├─ Cosine similarity against all embeddings
   │  └─ Get top N candidates
   ├─ Keyword Search:
   │  ├─ BM25 ranking on text content
   │  └─ Get top N candidates
   └─ Combine: combined_score = (alpha * semantic) + ((1-alpha) * keyword)

3. Apply Intelligence Boosts
   ├─ Status Intelligence:
   │  ├─ Parse checkbox patterns
   │  ├─ Detect progress keywords
   │  └─ Calculate status boost (0.8-1.2x)
   ├─ Temporal Intelligence:
   │  ├─ Extract time markers
   │  ├─ Calculate current relevance
   │  └─ Apply temporal boost (0.5-1.5x)
   ├─ Priority Intelligence:
   │  ├─ Match keyword multipliers
   │  ├─ Assess business hierarchy
   │  └─ Apply priority boost (1.0-2.5x)
   └─ Cap combined boost at 3.0x

4. Filter & Rank
   ├─ Apply domain filters (if specified)
   ├─ Apply status filters (if specified)
   ├─ Apply relevance threshold
   ├─ Sort by final boosted score
   └─ Return top K results
```

### Chunking Strategy

MBIE uses a **context-preserving hierarchical chunking** approach:

**File Size Categories:**
- **🟢 Small (<400 lines)**: Single chunk with full context
- **🟡 Medium (400-600 lines)**: Section-based chunking at `## Section` boundaries
- **🔴 Large (>600 lines)**: Extract executive summary + section-based chunking

**Chunking Algorithm:**
1. Parse markdown into section tree (H1, H2, H3 hierarchy)
2. Create navigation breadcrumbs (file.md → ## Section → ### Subsection)
3. For each section:
   - If section < chunk_size: Create single chunk
   - If section > chunk_size: Split at paragraph boundaries with overlap
4. Preserve metadata (size category, navigation path, line numbers)

**Example:**
```
File: memory-bank/features/calculator/technical-design.md (750 lines) 🔴

Chunks created:
1. Executive Summary (lines 1-50)
   navigation: technical-design.md → Executive Summary

2. Business Logic (lines 100-250)
   navigation: technical-design.md → ## Business Logic

3. Component Architecture (lines 251-450)
   navigation: technical-design.md → ## Component Architecture

4. Data Flow - Part 1 (lines 451-600)
   navigation: technical-design.md → ## Data Flow
   chunk_id: dataflow_1

5. Data Flow - Part 2 (lines 575-700) [50 line overlap]
   navigation: technical-design.md → ## Data Flow
   chunk_id: dataflow_2
```

### Intelligence Processing

#### Status Parsing Algorithm
```python
def parse_status(content: str) -> StatusInfo:
    # 1. Extract checkboxes
    completed = re.findall(r'\[x\]|\[X\]', content)
    pending = re.findall(r'\[ \]', content)
    in_progress = re.findall(r'\[-\]|\[~\]', content)

    # 2. Count progress keywords
    completed_kw = count_keywords(content, ['COMPLETED', 'DONE', '✅'])
    progress_kw = count_keywords(content, ['IN PROGRESS', 'CURRENT', '🔄'])
    pending_kw = count_keywords(content, ['PENDING', 'TODO', '📋'])

    # 3. Calculate confidence
    total_signals = len(completed) + len(pending) + len(in_progress) + \
                    completed_kw + progress_kw + pending_kw
    confidence = min(1.0, total_signals / 5.0)  # Normalize

    # 4. Determine status type (majority wins)
    if completed + completed_kw > (pending + pending_kw + in_progress + progress_kw):
        status = COMPLETED
    elif in_progress + progress_kw > (pending + pending_kw):
        status = IN_PROGRESS
    else:
        status = PENDING

    # 5. Calculate completion percentage
    total_items = len(completed) + len(pending) + len(in_progress)
    completion_pct = len(completed) / total_items if total_items > 0 else 0.0

    return StatusInfo(
        status_type=status,
        confidence=confidence,
        completion_percentage=completion_pct,
        checkbox_indicators=...,
        progress_markers=...
    )
```

#### Priority Scoring Algorithm
```python
def calculate_priority_boost(content: str, doc_path: str, config: dict) -> float:
    boost = 1.0

    # 1. Keyword multipliers
    for keyword, multiplier in config['keyword_multipliers'].items():
        if keyword in content:
            boost *= multiplier

    # 2. Business hierarchy (strategic > tactical > operational)
    if 'philosophy' in doc_path or 'vision' in doc_path:
        boost *= 1.3  # Strategic
    elif 'planning' in doc_path or 'quarterly' in doc_path:
        boost *= 1.1  # Tactical

    # 3. Client relevance
    for client_keyword in config['client_keywords']:
        if client_keyword in content:
            boost *= 1.5
            break

    # 4. Cap at maximum boost
    return min(boost, config['boost_cap'])
```

## Component Architecture

### Module Hierarchy

```
tools/memory_rag/
├── cli.py                      # CLI entry point
├── config.yml.template         # Configuration template
├── requirements_latest_stable.txt
└── core/
    ├── __init__.py
    ├── chunker.py              # MemoryBankChunker
    ├── embedder.py             # LocalEmbedder
    ├── searcher.py             # HybridSearcher
    ├── indexer.py              # IncrementalIndexer
    ├── intelligence.py         # Intelligence processors
    ├── learning.py             # Adaptive learning (Phase 2)
    └── analytics.py            # Usage analytics (Phase 2)
```

### Key Class Responsibilities

**MemoryBankChunker**
- Parse markdown documents
- Extract section hierarchy
- Create semantic chunks with navigation
- Categorize by file size (🟢🟡🔴)

**LocalEmbedder**
- Load sentence transformer model
- Generate 384-dimensional embeddings
- Cache embeddings (MD5 hash key)
- Batch processing for efficiency

**HybridSearcher**
- Initialize ChromaDB collection
- Perform semantic similarity search
- Perform BM25 keyword search
- Combine and rank results

**IncrementalIndexer**
- Manage index lifecycle
- Track file modifications
- Coordinate chunking and embedding
- Handle incremental updates

**IntelligenceProcessor**
- Coordinate all intelligence layers
- Parse status information
- Extract temporal context
- Calculate priority scores

## Integration Architecture

### File System Integration
```
Project Root
├── memory-bank/               # Documentation to index
│   ├── startHere.md
│   ├── features/
│   └── guides/
└── tools/
    └── memory_rag/            # MBIE installation
        ├── core/
        ├── tests/
        ├── index/             # ChromaDB storage (created on index)
        ├── cache/             # Embedding cache (created on index)
        ├── config.yml         # User configuration
        └── cli.py
```

### API Integration Points

**Python API Usage:**
```python
from tools.memory_rag.core import (
    MemoryBankChunker,
    LocalEmbedder,
    HybridSearcher,
    IncrementalIndexer
)

# Load configuration
config = load_yaml('tools/memory_rag/config.yml')

# Initialize components
indexer = IncrementalIndexer(config)
searcher = HybridSearcher(config, indexer.embedder)

# Index documents
indexed_count = indexer.full_index()

# Query
results = searcher.search(
    query="current week objectives",
    domain="current_work",
    status_filter="in_progress"
)

for result in results:
    print(f"{result.chunk.navigation_path}: {result.combined_score:.2f}")
```

**CLI Integration:**
```bash
# Index documentation
python cli.py index --config config.yml --full

# Query with filters
python cli.py query "authentication flow" \
    --status in_progress \
    --current-only \
    --domain technical

# View statistics
python cli.py stats --config config.yml
```

## Performance Considerations

### Optimization Strategies

1. **Embedding Cache**: MD5-based persistent cache prevents recomputation
2. **Batch Processing**: Process embeddings in batches of 32 for GPU efficiency
3. **Lazy Loading**: Load model only when needed (first query/index)
4. **Incremental Indexing**: Only reprocess changed files
5. **Result Limiting**: Cap search results at top_k (default: 10)

### Performance Benchmarks

- **Query Latency**: <500ms p95 for typical queries
- **Indexing Speed**: ~50 documents/minute (CPU)
- **Index Size**: ~2MB per 100 documents
- **Memory Usage**: ~500MB (model + index)
- **Scalability**: Tested up to 500 documents without degradation

### Resource Management

- **CPU Mode** (default): All platforms, ~2-3s per query
- **GPU Mode** (optional): 5-10x faster embedding generation
- **Memory Footprint**: ~500MB baseline + index size
- **Disk Space**: Model (500MB) + index (~2MB per 100 docs) + cache

---

**Next Steps**: See [implementation.md](./implementation.md) for development guide

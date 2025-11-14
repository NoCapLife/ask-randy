# Performance & Scalability Framework

**Purpose:** Performance SLAs, caching strategies, database optimization, and scaling patterns.

**When to use:** When setting performance targets, implementing caching, or planning for scale.

---

## 📁 Directory Structure

```
performance-scalability/
├── slas/                  # Response times, throughput, availability
├── caching/               # Redis, CDN, application-level caching
├── database/              # Indexing, query optimization, partitioning
├── background-jobs/       # Queuing, scheduling, async processing
└── examples/              # Performance optimization examples
```

---

## 🎯 What to Document

### SLAs (`slas/`)
**Files:** `response-times.md`, `throughput.md`, `availability.md`

**Quick Template:**
```markdown
# Performance SLAs

## API Response Times
| Endpoint | Target (p95) | Critical (p99) |
|----------|--------------|----------------|
| GET /api/users | <200ms | <500ms |
| POST /api/orders | <500ms | <1s |
| GET /api/reports | <2s | <5s |

## Throughput Targets
- Reads: 10,000 req/sec
- Writes: 1,000 req/sec
- Peak capacity: 50,000 concurrent users

## Availability
- Uptime: 99.9% (8.76 hours downtime/year)
- Planned maintenance: <4 hours/month
- RTO: 1 hour, RPO: 15 minutes
```

### Caching (`caching/`)
**Files:** `cache-strategies.md`, `cache-invalidation.md`, `cdn-config.md`

**Quick Template:**
```markdown
# Caching Strategy

## Cache Layers
1. **CDN:** Static assets (images, CSS, JS)
2. **Application cache:** API responses (Redis)
3. **Database cache:** Query results (built-in)

## Cache Keys
- User data: `user:{user_id}`
- Product catalog: `product:{product_id}`
- Search results: `search:{query_hash}`

## TTL Configuration
- Static assets: 1 year (immutable URLs)
- User sessions: 24 hours
- Product data: 1 hour
- Search results: 5 minutes

## Invalidation Strategy
- **Time-based:** TTL expiration
- **Event-based:** Clear cache on entity update
- **Manual:** Admin cache clear endpoint
```

### Database (`database/`)
**Files:** `indexing-strategy.md`, `query-optimization.md`, `partitioning.md`

---

## 🎓 Quick Best Practices

1. **Measure First:** Profile before optimizing
2. **Cache Aggressively:** But invalidate correctly
3. **Index Strategically:** Index queries, not tables
4. **Background Work:** Move heavy processing to jobs
5. **Scale Horizontally:** Prefer adding servers over bigger servers

---

**Last Updated:** 2025-10-14
**Review Frequency:** Monthly

---
title: Archive - Deprecated Documentation
type: archive
status: inactive
last_updated: 2025-01-10
---

# Archive - Deprecated Documentation

**Purpose**: Storage for deprecated or superseded documentation.
**Audience**: Developers seeking historical context.

## Archiving Guidelines

### When to Archive
- Feature has been sunset or removed
- Documentation superseded by newer version
- Experimental approach abandoned
- Decision reversed (keep for historical reference)

### How to Archive
1. Move file from original location to `/archive/[year]/[month]/`
2. Add `status: archived` to frontmatter
3. Add `archived_date` and `reason` fields
4. Update original location's index to point here
5. Add entry to this README

### Archive Structure
\`\`\`
archive/
├── 2024/
│   ├── 01-january/
│   │   └── old-feature-spec.md
│   └── 12-december/
│       └── deprecated-api.md
├── 2025/
│   └── 01-january/
└── README.md (this file)
\`\`\`

### Retention Policy
- Keep archived docs for 2 years minimum
- Review annually for permanent deletion
- Never delete docs with compliance implications

## Currently Archived Items

*No items archived yet - this is a new memory-bank.*

## Related Documentation
- [← Back to startHere.md](../startHere.md)

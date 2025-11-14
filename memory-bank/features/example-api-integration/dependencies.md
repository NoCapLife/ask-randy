---
title: API Integration - Dependencies
type: dependencies
feature: example-api-integration
last_updated: 2025-01-10
---

# API Integration Feature - Dependencies

[← Back](./README.md) | [← Previous](./decisions.md)

## Direct Dependencies

\`\`\`json
{
  "stripe": "^14.0.0",
  "axios": "^1.6.0",
  "axios-retry": "^4.0.0",
  "opossum": "^8.1.0"
}
\`\`\`

**Purpose**:
- `stripe`: Official Stripe SDK
- `axios`: HTTP client
- `axios-retry`: Retry logic
- `opossum`: Circuit breaker pattern

## External Services

### Stripe API
- **Version**: 2024-11-20
- **Auth**: OAuth 2.0
- **Rate Limits**: 100 req/sec (burst 1000)
- **SLA**: 99.99% uptime

### Redis (for idempotency)
- **Purpose**: Store processed webhook IDs
- **TTL**: 24 hours
- **Memory**: 256MB minimum

## API Compatibility
- Minimum Stripe API version: 2023-10-16
- Webhook API version: v3
- Node.js: >= 18.0.0

[← Back](./README.md) | [← Previous](./decisions.md)

**API Integration Example Complete**: All 8 files created with focus on integration patterns.

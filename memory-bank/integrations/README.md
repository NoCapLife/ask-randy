# Integrations Framework

**Purpose:** API design standards, external system integrations, versioning strategies, and webhook patterns.

**When to use:** When designing APIs, integrating external services, or planning API versioning.

---

## 📁 Directory Structure

```
integrations/
├── api-design/            # REST, GraphQL, webhooks
├── external-systems/      # Payment, shipping, accounting integrations
├── versioning/            # API versioning and deprecation
└── examples/              # Integration examples
```

---

## 🎯 What to Document

### API Design (`api-design/`)
**Files:** `rest-api-standards.md`, `graphql-schema.md`, `webhooks.md`

**Quick Template (REST API):**
```markdown
# REST API Standards

## URL Structure
- Resource-based: `/api/v1/users/{id}`
- Actions as sub-resources: `/api/v1/orders/{id}/cancel`
- Avoid verbs in URLs (use HTTP methods)

## HTTP Methods
- GET: Retrieve resource(s)
- POST: Create resource
- PUT: Replace resource
- PATCH: Update resource
- DELETE: Remove resource

## Response Format
\`\`\`json
{
  "data": { ... },
  "meta": {
    "timestamp": "2025-10-14T12:00:00Z",
    "request_id": "uuid"
  },
  "errors": null
}
\`\`\`

## Status Codes
- 200: Success
- 201: Created
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Not found
- 500: Server error

## Pagination
\`\`\`
GET /api/v1/users?page=1&limit=50
Response headers:
  X-Total-Count: 1000
  X-Page: 1
  X-Per-Page: 50
\`\`\`

## Authentication
- Bearer token: `Authorization: Bearer {token}`
- API key: `X-API-Key: {key}`
```

### External Systems (`external-systems/`)
**Files:** `payment-gateways.md`, `shipping-providers.md`, `email-service.md`

**Quick Template:**
```markdown
# [Service Name] Integration

## Overview
- **Service:** Stripe Payment Gateway
- **Purpose:** Payment processing
- **Documentation:** https://stripe.com/docs

## Configuration
\`\`\`env
STRIPE_PUBLIC_KEY=pk_live_...
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
\`\`\`

## API Endpoints Used
- `POST /v1/payment_intents` - Create payment
- `GET /v1/payment_intents/{id}` - Get status
- Webhook: `/webhook/stripe` - Payment events

## Error Handling
- Network failures: Retry up to 3 times
- Authentication errors: Alert dev team
- Rate limits: Exponential backoff

## Monitoring
- Track success rate
- Monitor response times
- Alert on failures >5%
```

### Versioning (`versioning/`)
**Files:** `versioning-strategy.md`, `deprecation-policy.md`, `migration-guides.md`

**Quick Template:**
```markdown
# API Versioning Strategy

## Version Format
- URL-based: `/api/v1/`, `/api/v2/`
- Major version only in URL
- Minor/patch changes backward compatible

## Breaking Changes
Require new major version:
- Removing endpoints
- Changing response structure
- Changing authentication method

## Deprecation Process
1. **Announce** (6 months before): Email + docs
2. **Mark deprecated** (3 months before): Response header
3. **Sunset** (on schedule): Remove old version

## Example Header
\`\`\`
Deprecation: Sat, 1 Apr 2026 00:00:00 GMT
Sunset: Sat, 1 Jul 2026 00:00:00 GMT
Link: </api/v2/users>; rel="successor"
\`\`\`
```

---

## 🎓 Quick Best Practices

1. **Consistent API Design:** Follow REST/GraphQL conventions
2. **Comprehensive Documentation:** OpenAPI/Swagger specs
3. **Graceful Degradation:** Handle external service failures
4. **Version Carefully:** Don't break existing clients
5. **Monitor Integrations:** Track health of all external services

---

**Last Updated:** 2025-10-14
**Review Frequency:** Quarterly

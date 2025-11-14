---
title: Dashboard Feature - Dependencies
type: dependencies
feature: example-dashboard
category: example
status: template-example
last_updated: 2025-01-10
maintainers: ["engineering-team", "platform-team"]
---

# Dashboard Feature - Dependencies

**Purpose**: Document all dependencies, integrations, and version requirements for enterprise dashboard.
**Audience**: Engineers, DevOps, platform teams.
**File Size**: 🟡 Medium (200 lines) - Complex dependency graph.

[← Back to Dashboard Hub](./README.md) | [← Previous: Decisions](./decisions.md)

---

## 📦 Direct Dependencies

### Core Framework
```json
{
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "typescript": "^5.0.0",
  "next": "^14.0.0"
}
```

**Update Policy**: Pin major versions, review quarterly, test thoroughly before upgrading.

### State Management
```json
{
  "zustand": "^4.4.0",
  "immer": "^10.0.0",
  "@tanstack/react-query": "^5.0.0"
}
```

**Purpose**:
- `zustand`: Global state management (layout, filters, preferences)
- `immer`: Immutable state updates
- `@tanstack/react-query`: API data fetching and caching

**Critical**: React Query version must support React 18+ for streaming features.

### Real-Time Communication
```json
{
  "socket.io-client": "^4.6.0",
  "reconnecting-websocket": "^4.4.0"
}
```

**Purpose**: WebSocket connections with automatic reconnection.
**Server Requirement**: socket.io-server ^4.6.0 (matching client version).

### Charts & Visualization
```json
{
  "recharts": "^2.10.0",
  "d3": "^7.8.0",
  "d3-scale": "^4.0.2",
  "d3-array": "^3.2.4"
}
```

**Purpose**:
- `recharts`: Primary chart library (declarative React charts)
- `d3`: Custom visualizations (20% of charts)
- Specific D3 modules to reduce bundle size

**Bundle Impact**: Recharts (93KB) + D3 modules (~50KB) = 143KB gzipped.

### Layout & Interactions
```json
{
  "react-grid-layout": "^1.4.0",
  "@dnd-kit/core": "^6.0.0",
  "@dnd-kit/sortable": "^7.0.0",
  "@dnd-kit/utilities": "^3.2.0"
}
```

**Purpose**:
- `react-grid-layout`: Responsive grid system for widgets
- `@dnd-kit/*`: Drag-and-drop interactions

**Performance**: Tested with 12+ widgets, smooth 60fps interactions.

### Date & Time Handling
```json
{
  "date-fns": "^2.30.0"
}
```

**Why not moment.js**: date-fns is tree-shakeable (~15KB vs 200KB+).

### Export Functionality
```json
{
  "jspdf": "^2.5.0",
  "jspdf-autotable": "^3.7.0",
  "papaparse": "^5.4.0"
}
```

**Purpose**:
- `jspdf`: PDF generation (visual exports)
- `papaparse`: CSV parsing and generation

## 🧪 Development Dependencies

### Testing
```json
{
  "vitest": "^1.0.0",
  "@testing-library/react": "^14.0.0",
  "@testing-library/user-event": "^14.0.0",
  "@testing-library/jest-dom": "^6.0.0",
  "@vitest/ui": "^1.0.0",
  "jsdom": "^23.0.0",
  "playwright": "^1.40.0",
  "k6": "^0.48.0"
}
```

**Purpose**:
- `vitest`: Unit and integration tests
- `@testing-library/*`: React component testing
- `playwright`: E2E testing
- `k6`: Load and performance testing

**Critical**: k6 runs separately (not in package.json, installed globally).

### Code Quality
```json
{
  "eslint": "^8.50.0",
  "eslint-plugin-react": "^7.33.0",
  "eslint-plugin-react-hooks": "^4.6.0",
  "eslint-plugin-jsx-a11y": "^6.8.0",
  "prettier": "^3.0.0",
  "typescript-eslint": "^6.0.0"
}
```

### Accessibility
```json
{
  "axe-core": "^4.8.0",
  "jest-axe": "^8.0.0",
  "@axe-core/playwright": "^4.8.0"
}
```

## 🌐 Backend Dependencies

### API Server
```json
{
  "express": "^4.18.0",
  "socket.io": "^4.6.0",
  "redis": "^4.6.0",
  "ioredis": "^5.3.0",
  "pg": "^8.11.0",
  "jsonwebtoken": "^9.0.0"
}
```

**Purpose**:
- `express`: HTTP API server
- `socket.io`: WebSocket server
- `redis`/`ioredis`: Caching and pub/sub
- `pg`: PostgreSQL client
- `jsonwebtoken`: JWT authentication

### Data Processing
```json
{
  "bull": "^4.11.0",
  "pg-query-stream": "^4.5.0"
}
```

**Purpose**:
- `bull`: Background job processing (Redis-backed queue)
- `pg-query-stream`: Streaming large query results

## 🔧 Infrastructure Dependencies

### Required Services

#### PostgreSQL
- **Version**: 14+
- **Purpose**: Primary data store for metrics, user data, layouts
- **Extensions**: TimescaleDB (for time-series metrics)
- **Connection Pool**: 20 connections per API instance

#### Redis
- **Version**: 7.0+
- **Purpose**: Caching (L3), pub/sub (real-time updates), session storage
- **Memory**: 4GB minimum, 16GB recommended
- **Persistence**: AOF enabled (appendonly yes)

#### WebSocket Server
- **Scaling**: Sticky sessions required (socket.io)
- **Load Balancer**: Must support WebSocket upgrade

#### CDN
- **Purpose**: Static assets, chart images
- **Suggested**: CloudFlare, AWS CloudFront
- **Cache TTL**: 1 year for hashed assets

### Browser Requirements
```
Minimum Supported:
- Chrome/Edge: >= 100
- Firefox: >= 100
- Safari: >= 15.4

Required Features:
- ES2022 support
- WebSocket API
- IndexedDB API
- CSS Grid
- Intersection Observer API
```

## 🔗 Integration Points

### External APIs

#### Analytics Data Sources
```typescript
interface DataSourceConfig {
  type: 'rest' | 'graphql' | 'grpc';
  endpoint: string;
  authentication: 'oauth2' | 'api-key' | 'jwt';
  rateLimits: {
    requests: number;
    window: number; // milliseconds
  };
}
```

**Integrated Sources** (examples):
- Google Analytics API
- Stripe API (revenue data)
- Segment API (event tracking)
- Custom internal APIs

**Rate Limiting**: Client-side throttling to respect API limits.

#### Authentication Providers
- **Primary**: OAuth 2.0 (Auth0, Okta, Google Workspace)
- **Secondary**: SAML 2.0 (enterprise SSO)
- **MFA**: TOTP support (optional)

### Internal Services

#### Notification Service
- **Email**: SendGrid, AWS SES
- **Slack**: Slack API with incoming webhooks
- **SMS**: Twilio (optional)
- **Push**: Firebase Cloud Messaging (mobile apps)

#### Audit Logging
- **Service**: Elasticsearch or custom audit API
- **Retention**: 2 years (compliance requirement)
- **Events**: All data access, permission changes, config changes

## 📊 Dependency Management

### Version Pinning Strategy
```
- Framework dependencies: Pin major (^)
- State management: Pin major (^)
- Chart libraries: Pin minor (~)
- Security-critical: Pin exact version
```

### Security Updates
```bash
# Weekly automated scan
npm audit

# Monthly dependency updates
npm outdated
npm update --save

# Security-only updates (immediate)
npm audit fix
```

### Bundle Size Monitoring
```bash
# Build analysis
npm run build:analyze

# Size limits (enforced in CI)
Main bundle: <300KB gzipped
Vendor bundle: <500KB gzipped
Chart bundle: <150KB gzipped
Total initial load: <1MB gzipped
```

### Deprecation Policy
```
1. Monitor dependency deprecation notices
2. Plan migration within 1 quarter
3. Complete migration before EOL
4. Test thoroughly in staging
5. Gradual rollout to production
```

## 🚨 Critical Dependencies

### High Priority (Security/Performance Impact)
```
react → Core framework
next → Server framework
zustand → State management
@tanstack/react-query → Data fetching
socket.io-client → Real-time updates
recharts → Visualizations
```

**Update Schedule**: Review monthly, update quarterly.
**Breaking Changes**: Require full regression testing suite.

### Medium Priority
```
date-fns → Date utilities
@dnd-kit/* → Drag-and-drop
jspdf → PDF export
```

**Update Schedule**: Review quarterly, update bi-annually.

### Low Priority
```
Development dependencies
Testing utilities
Build tools
```

**Update Schedule**: Update as needed, no strict schedule.

## 🔍 Compatibility Matrix

| Dependency | Min Version | Max Tested | Breaking Changes |
|------------|-------------|------------|------------------|
| React | 18.2.0 | 18.2.0 | Concurrent features required |
| Next.js | 14.0.0 | 14.1.0 | App Router only |
| Zustand | 4.4.0 | 4.5.0 | Persist middleware API |
| React Query | 5.0.0 | 5.17.0 | Query key structure |
| Recharts | 2.10.0 | 2.12.0 | None |
| Socket.io | 4.6.0 | 4.6.1 | Server version must match |

## 🔗 Related Documentation

- [Technical Design](./technical-design.md) - How dependencies are used
- [Implementation](./implementation.md) - Integration guides
- [Decisions](./decisions.md) - Why these dependencies chosen

---

[← Back to Dashboard Hub](./README.md) | [← Previous: Decisions](./decisions.md)

**Dependency Note**: This is a complex feature with many dependencies. Maintain security and keep bundle size optimized through code splitting and tree shaking.

**Dashboard Example Complete**: All 8 files created for complex enterprise dashboard feature.

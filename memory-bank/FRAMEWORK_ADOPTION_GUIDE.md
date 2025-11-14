# Framework Adoption Guide

**Purpose:** Guide for when and how to use each of the 6 scalability frameworks.

**Last Updated:** 2025-10-14

---

## Quick Decision Matrix

| Your Need | Framework to Use |
|-----------|------------------|
| Documenting database tables, entities, relationships | **Data Architecture** |
| Defining multi-step processes, approvals, state transitions | **Business Processes** |
| Implementing access control, compliance, auditing | **Security & Compliance** |
| Planning testing strategy, managing test data | **Testing & QA** |
| Setting performance targets, caching, optimization | **Performance & Scalability** |
| Designing APIs, external integrations | **Integrations** |

---

## Framework 1: Data Architecture

### When to Use
✅ **Use when:**
- Designing new database entities/tables
- Documenting existing data models
- Planning schema migrations
- Defining data relationships (foreign keys, joins)
- Establishing data governance policies
- Implementing row-level security (RLS)
- Setting up audit trails for data changes
- Defining data validation rules

❌ **Don't use when:**
- Documenting UI components
- Writing business logic code
- Planning API endpoints (use Integrations instead)
- Defining user workflows (use Business Processes instead)

### Common Use Cases

**1. New Feature with Database Changes**
```
Scenario: Adding a "Teams" feature to your app

Steps:
1. Document entity in data-architecture/schema/entities/team.md
2. Define relationships in data-architecture/schema/relationships/team-relationships.md
3. Create migration in data-architecture/schema/migrations/YYYYMMDD-add-teams.md
4. Define RLS policies in data-architecture/data-governance/access-control/rls-policies.md
```

**2. Refactoring Existing Schema**
```
Scenario: Splitting "users" table into "users" and "profiles"

Steps:
1. Document new schema in data-architecture/schema/entities/
2. Create migration plan in data-architecture/schema/migrations/
3. Update relationships documentation
4. Plan data migration strategy
```

**3. Implementing Data Governance**
```
Scenario: Need to comply with GDPR data retention

Steps:
1. Document data classification in data-architecture/data-governance/data-quality/
2. Define retention policies
3. Document anonymization procedures
4. Create audit requirements
```

### Example: Complete Entity Documentation

**File:** `memory-bank/data-architecture/schema/entities/user.md`

```markdown
# User Entity

## Purpose
Core user authentication and profile management.

## Schema
| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| id | uuid | NO | gen_random_uuid() | Primary key |
| email | text | NO | - | Unique email address |
| name | text | YES | - | Display name |
| created_at | timestamptz | NO | now() | Account creation |
| role | text | NO | 'user' | user, admin, super_admin |

## Relationships
- Has many: sessions (one-to-many)
- Has one: profile (one-to-one)
- Belongs to many: teams (many-to-many through team_members)

## RLS Policies
- Users can SELECT their own record
- Users can UPDATE their own record (except role)
- Only admins can INSERT or DELETE users

## Audit Requirements
- Log all role changes
- Track last login timestamp
- Monitor failed login attempts
```

---

## Framework 2: Business Processes

### When to Use
✅ **Use when:**
- Documenting multi-step workflows
- Defining approval chains
- Creating state machines
- Planning complex business logic
- Documenting decision trees
- Defining SLA requirements for processes
- Mapping cross-system workflows

❌ **Don't use when:**
- Documenting simple CRUD operations
- Writing API documentation (use Integrations)
- Defining UI flows (may use, but consider UX docs)
- Documenting database queries

### Common Use Cases

**1. Order Fulfillment Process**
```
Scenario: E-commerce order from placement to delivery

Use: business-processes/workflows/order-fulfillment-workflow.md

Document:
- Each step (order → payment → inventory → shipment → delivery)
- Decision points (payment success? inventory available?)
- Actors involved (customer, payment gateway, warehouse, carrier)
- SLAs (order to shipment < 24 hours)
- Error handling (payment failed, out of stock)
```

**2. Approval Workflow**
```
Scenario: Expense approval based on amount and department

Use: business-processes/approval-chains/expense-approval-chain.md

Document:
- Approval levels (manager → director → executive)
- Amount thresholds ($500, $5k, $10k)
- Timeout behavior (auto-approve, escalate, reject)
- Notification templates
```

**3. Document Lifecycle State Machine**
```
Scenario: Document goes through draft → review → published → archived

Use: business-processes/state-machines/document-state-machine.md

Document:
- All states
- Valid transitions
- Transition triggers (actions/events)
- Permissions per state
- Business rules for transitions
```

### Example: Workflow Documentation

**File:** `memory-bank/business-processes/workflows/user-onboarding-workflow.md`

```markdown
# User Onboarding Workflow

## Steps
1. Sign Up (self-service)
2. Email Verification
3. Profile Completion
4. Welcome Email
5. First Login

## Duration
Target: 5 minutes (user active time)
Total: up to 24 hours (including email verification)

## Decision Points
- Email verified? → Yes: Continue | No: Resend email
- Profile complete? → Yes: Send welcome | No: Prompt completion

## SLAs
- Verification email delivery: <30 seconds
- Welcome email delivery: <1 minute after profile completion
```

---

## Framework 3: Security & Compliance

### When to Use
✅ **Use when:**
- Implementing role-based access control (RBAC)
- Planning security architecture
- Documenting compliance requirements (SOC 2, GDPR, HIPAA)
- Defining audit logging requirements
- Creating security policies
- Planning penetration testing
- Documenting incident response procedures

❌ **Don't use when:**
- Writing application code (reference this, don't duplicate)
- Documenting API authentication (use Integrations)
- Database RLS (use Data Architecture, but may cross-reference here)

### Common Use Cases

**1. RBAC Implementation**
```
Scenario: Setting up roles and permissions for SaaS app

Use: security-compliance/access-control/rbac-model.md

Document:
- Role hierarchy
- Permission matrix
- Role assignment rules
- Default permissions
```

**2. GDPR Compliance**
```
Scenario: Implementing GDPR data rights

Use: security-compliance/compliance/gdpr-compliance.md

Document:
- Right to access implementation
- Right to erasure (delete account)
- Right to data portability
- Consent management
- Data breach response plan
```

**3. Audit Logging**
```
Scenario: Track all sensitive data access

Use: security-compliance/audit-logging/audit-requirements.md

Document:
- What to log (authentication, data access, admin actions)
- Log format and schema
- Retention policy
- Alert thresholds
```

### Example: RBAC Documentation

**File:** `memory-bank/security-compliance/access-control/rbac-model.md`

```markdown
# RBAC Model

## Roles
- **User**: Basic access, can manage own data
- **Admin**: Organization admin, can manage users
- **Super Admin**: Platform admin, full access

## Permission Matrix
| Resource | User | Admin | Super Admin |
|----------|------|-------|-------------|
| Own profile | CRUD | CRUD | CRUD |
| Other users | R | CRUD (org) | CRUD (all) |
| Settings | R | RU (org) | CRUD (all) |
| Audit logs | - | R (org) | R (all) |

Legend: C=Create, R=Read, U=Update, D=Delete
```

---

## Framework 4: Testing & QA

### When to Use
✅ **Use when:**
- Planning testing strategy
- Defining test coverage requirements
- Managing test data
- Setting up CI/CD testing
- Documenting QA processes
- Planning performance testing
- Creating E2E test scenarios

❌ **Don't use when:**
- Writing actual test code (reference this for strategy)
- Debugging specific issues (use issue tracker)
- Planning production monitoring (use Performance & Scalability)

### Common Use Cases

**1. Feature Testing Strategy**
```
Scenario: Testing new "Teams" feature

Use: testing-qa/strategies/integration-testing.md

Document:
- Unit tests needed (per component)
- Integration tests (component interactions)
- E2E tests (user workflows)
- Test data requirements
- Coverage targets
```

**2. Test Data Management**
```
Scenario: Need realistic test data for development

Use: testing-qa/test-data/data-generation.md

Document:
- Data generation scripts
- Anonymization rules
- Test database seeding
- Data refresh procedures
```

**3. CI/CD Test Automation**
```
Scenario: Automated testing in GitHub Actions

Use: testing-qa/automation/ci-cd-testing.md

Document:
- Test execution order
- Parallel vs sequential tests
- Environment setup
- Failure handling
- Performance budgets
```

### Example: Testing Strategy

**File:** `memory-bank/testing-qa/strategies/unit-testing.md`

```markdown
# Unit Testing Strategy

## Coverage Target
Minimum: 80% overall, 90% for core/ directory

## Standards
- Co-located with source (same directory)
- File naming: `{module}.test.ts`
- Test naming: `test_{function}_{behavior}_{condition}`

## Mocking Strategy
- Mock external services (APIs, databases)
- Use real implementations for core utilities
- Stub time-dependent functions

## Example
\`\`\`typescript
// user.test.ts
describe('User', () => {
  it('should validate email format', () => {
    expect(validateEmail('test@example.com')).toBe(true);
    expect(validateEmail('invalid')).toBe(false);
  });
});
\`\`\`
```

---

## Framework 5: Performance & Scalability

### When to Use
✅ **Use when:**
- Setting performance SLAs
- Planning caching strategy
- Optimizing database queries
- Designing for scale
- Planning background job processing
- Load testing
- Monitoring and alerting

❌ **Don't use when:**
- Writing optimization code (reference this for requirements)
- Debugging performance issues (use profiling tools)
- Planning infrastructure (may overlap, but focus on app-level)

### Common Use Cases

**1. Performance SLAs**
```
Scenario: Define acceptable response times for all APIs

Use: performance-scalability/slas/response-times.md

Document:
- Target response times (p50, p95, p99)
- Throughput requirements
- Availability targets
- Degradation gracefully strategies
```

**2. Caching Strategy**
```
Scenario: Implement Redis caching for API responses

Use: performance-scalability/caching/cache-strategies.md

Document:
- What to cache
- Cache keys structure
- TTL policies
- Invalidation strategy
- Cache warming
```

**3. Database Optimization**
```
Scenario: Slow queries identified in production

Use: performance-scalability/database/query-optimization.md

Document:
- Identified slow queries
- Index strategy
- Query rewrite patterns
- Partitioning strategy
- Connection pooling
```

### Example: Performance SLA

**File:** `memory-bank/performance-scalability/slas/response-times.md`

```markdown
# API Response Time SLAs

## Targets
| Endpoint Type | p50 | p95 | p99 |
|---------------|-----|-----|-----|
| Simple GET | 50ms | 100ms | 200ms |
| Complex GET | 200ms | 500ms | 1s |
| POST/PUT | 100ms | 300ms | 500ms |
| Reports | 1s | 3s | 5s |

## Monitoring
- Alert if p95 > target for 5 minutes
- Page if p99 > 2x target for 1 minute
- Track trends weekly

## Actions
- p95 exceeded: Investigate, optimize
- p99 exceeded: Immediate review, add caching
- Consistent failures: Refactor or scale
```

---

## Framework 6: Integrations

### When to Use
✅ **Use when:**
- Designing REST or GraphQL APIs
- Integrating external services
- Planning webhooks
- Defining API versioning strategy
- Documenting third-party integrations
- Planning authentication/authorization for APIs

❌ **Don't use when:**
- Documenting internal function calls (use code comments)
- Planning database schemas (use Data Architecture)
- Defining business workflows (use Business Processes)

### Common Use Cases

**1. REST API Design**
```
Scenario: Designing public API for your application

Use: integrations/api-design/rest-api-standards.md

Document:
- URL structure conventions
- HTTP method usage
- Request/response formats
- Error handling
- Rate limiting
- Authentication
```

**2. Third-Party Integration**
```
Scenario: Integrating Stripe for payments

Use: integrations/external-systems/stripe-integration.md

Document:
- API endpoints used
- Webhook handling
- Error scenarios
- Retry logic
- Monitoring
```

**3. API Versioning**
```
Scenario: Planning API v2 with breaking changes

Use: integrations/versioning/versioning-strategy.md

Document:
- Version format (URL vs header)
- Deprecation timeline
- Migration guide
- Breaking changes
- Backward compatibility plan
```

### Example: API Integration

**File:** `memory-bank/integrations/external-systems/sendgrid-integration.md`

```markdown
# SendGrid Email Integration

## Purpose
Transactional email delivery for user notifications

## Configuration
\`\`\`env
SENDGRID_API_KEY=sg_...
SENDGRID_FROM_EMAIL=noreply@yourdomain.com
\`\`\`

## Endpoints Used
- POST /v3/mail/send - Send email
- GET /v3/mail/batch/{batch_id} - Check status

## Error Handling
- Rate limit (429): Exponential backoff
- Invalid email (400): Log and skip
- Network error: Retry 3 times, then queue for later

## Monitoring
- Track send success rate (target: >99.5%)
- Alert if rate < 95% for 10 minutes
- Monitor bounce and spam rates
```

---

## Framework Interaction Patterns

### Common Combinations

**Feature Development Flow:**
1. **Data Architecture**: Define entities and relationships
2. **Business Processes**: Document workflows using those entities
3. **Security & Compliance**: Add access control and audit requirements
4. **Testing & QA**: Plan testing strategy
5. **Performance & Scalability**: Set performance targets
6. **Integrations**: Document any external API interactions

**Example: Building a "Purchase Orders" Feature**

```
1. Data Architecture:
   - entities/purchase_order.md
   - entities/purchase_order_item.md
   - relationships/purchase-order-relationships.md
   - migrations/YYYYMMDD-add-purchase-orders.md

2. Business Processes:
   - workflows/purchase-order-workflow.md
   - approval-chains/purchase-order-approval.md
   - state-machines/purchase-order-state-machine.md

3. Security & Compliance:
   - access-control/purchase-order-permissions.md
   - audit-logging/purchase-order-audit.md

4. Testing & QA:
   - strategies/purchase-order-testing.md
   - test-data/purchase-order-test-data.md

5. Performance & Scalability:
   - slas/purchase-order-performance.md
   - caching/purchase-order-caching.md

6. Integrations:
   - external-systems/supplier-api-integration.md
   - api-design/purchase-order-api.md
```

---

## Adoption Best Practices

### 1. Start Small
Don't try to document everything at once. Pick one framework and one use case.

**Recommended First Framework:** Data Architecture (most foundational)

### 2. Iterative Documentation
Document as you build, not after. Keep documentation in sync with code.

### 3. Cross-Reference
Link between frameworks liberally:
```markdown
See also:
- Data Architecture: entities/user.md
- Security & Compliance: access-control/user-permissions.md
```

### 4. Use Templates
Each framework README has templates. Start with those and customize.

### 5. Update Regularly
Set a schedule:
- **Weekly**: Update for current sprint work
- **Monthly**: Review for completeness
- **Quarterly**: Audit for accuracy and prune outdated docs

---

## Decision Flowchart

```
Need to document something?
│
├─ Database/data related? → Data Architecture
├─ Multi-step process? → Business Processes
├─ Security/access/compliance? → Security & Compliance
├─ Testing approach? → Testing & QA
├─ Performance concern? → Performance & Scalability
└─ API or external system? → Integrations
```

---

## Getting Started Checklist

### For New Projects
- [ ] Set up all 6 framework directories (already done in template)
- [ ] Read through all 6 framework READMEs
- [ ] Pick your first framework to adopt (recommend: Data Architecture)
- [ ] Document your first entity/process/integration
- [ ] Link related documentation across frameworks
- [ ] Index with MBIE: `python3 cli.py index`
- [ ] Test searchability: `python3 cli.py query "your keyword"`

### For Existing Projects
- [ ] Audit existing documentation
- [ ] Map existing docs to appropriate frameworks
- [ ] Identify gaps
- [ ] Prioritize gaps by impact
- [ ] Incrementally migrate and fill gaps
- [ ] Maintain both old and new during transition
- [ ] Deprecate old docs once new ones are complete

---

## FAQ

**Q: Do I need to use all 6 frameworks?**
A: No. Use what makes sense for your project. A simple CRUD app might only need Data Architecture and Testing & QA.

**Q: Can I customize the framework structure?**
A: Yes. These are templates. Add subdirectories, modify templates, make it work for you.

**Q: Should I document everything or just complex features?**
A: Focus on complex, frequently-referenced, or high-risk areas. Simple CRUD operations don't need extensive documentation.

**Q: How do I keep documentation in sync with code?**
A: Make documentation updates part of your PR checklist. If you change the code, update the docs.

**Q: What if I'm not sure which framework to use?**
A: Start with the decision matrix at the top of this guide. When in doubt, ask: "What question is this documentation answering?"

---

## Resources

- **Framework READMEs**: See each framework's README for detailed templates
- **Examples**: Check `examples/` directories in each framework
- **MBIE**: Use `python3 cli.py query "framework name"` to search documentation
- **Issues**: Report framework questions at https://github.com/virtuoso902/Template/issues

---

**Last Updated:** 2025-10-14
**Maintainer:** Development Team
**Review Frequency:** Quarterly

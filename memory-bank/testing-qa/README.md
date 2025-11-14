# Testing & Quality Assurance Framework

**Purpose:** Testing strategies, test data management, automation patterns, and quality standards.

**When to use:** When designing test strategies, creating test data, or setting up automated testing.

---

## 📁 Directory Structure

```
testing-qa/
├── strategies/            # Unit, integration, E2E, performance testing
├── test-data/             # Test data generation and management
├── automation/            # CI/CD testing, regression suites
└── examples/              # Example test implementations
```

---

## 🎯 What to Document

### Testing Strategies (`strategies/`)

**Files:**
- `unit-testing.md` - Unit test standards per module
- `integration-testing.md` - Cross-module testing
- `e2e-testing.md` - End-to-end business process testing
- `performance-testing.md` - Load, stress, and scalability testing

**Quick Template:**
```markdown
# [Test Type] Strategy

## Scope
What we test and why.

## Standards
- Coverage target: X%
- Test file location: co-located vs. separate
- Naming conventions: `*.test.ts`, `*.spec.ts`
- Mocking strategy: When to mock vs. real dependencies

## Examples
\`\`\`typescript
// Example test structure
describe('FeatureName', () => {
  beforeEach(() => {
    // Setup
  });

  it('should handle happy path', () => {
    // Test implementation
  });

  it('should handle edge case', () => {
    // Test implementation
  });
});
\`\`\`

## CI/CD Integration
- When tests run (on PR, on merge, nightly)
- Failure handling
- Performance budgets
```

---

### Test Data (`test-data/`)

**Files:**
- `data-generation.md` - How to generate realistic test data
- `data-management.md` - Test data lifecycle
- `data-sanitization.md` - Removing PII from production data

**Quick Template:**
```markdown
# Test Data Management

## Test Data Sources
1. **Synthetic data:** Generated programmatically
2. **Anonymized production:** Sanitized real data
3. **Manual fixtures:** Hand-crafted for specific scenarios

## Data Generation Patterns
\`\`\`typescript
// Factory pattern for test data
const createTestUser = (overrides = {}) => ({
  id: uuid(),
  email: `test-${uuid()}@example.com`,
  name: faker.name.fullName(),
  created_at: new Date(),
  ...overrides
});
\`\`\`

## Test Database Setup
- Separate test database
- Reset between test runs
- Seed data for E2E tests

## Data Sanitization Rules
- Email: Replace with test domain
- Names: Use faker library
- PII fields: Remove or anonymize
- Sensitive data: Never include in tests
```

---

### Automation (`automation/`)

**Files:**
- `ci-cd-testing.md` - Automated testing in pipelines
- `regression-suite.md` - Automated regression testing
- `test-reporting.md` - Test results and metrics

---

## 🎓 Quick Best Practices

1. **Test Pyramid:** Many unit tests, fewer integration, few E2E
2. **Fast Feedback:** Unit tests <1s, integration <10s, E2E <5min
3. **Reliable Tests:** No flaky tests - fix or remove
4. **Clear Assertions:** One logical assertion per test
5. **Test Data Isolation:** Each test creates its own data

---

**Last Updated:** 2025-10-14
**Review Frequency:** Quarterly

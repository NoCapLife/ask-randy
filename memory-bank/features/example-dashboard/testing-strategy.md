---
title: Dashboard Feature - Testing Strategy
type: testing-strategy
feature: example-dashboard
category: example
status: template-example
last_updated: 2025-01-10
qa_owners: ["qa-team", "engineering"]
coverage_target: 85
---

# Dashboard Feature - Testing Strategy

**Purpose**: Comprehensive testing strategy for enterprise dashboard.
**Audience**: QA engineers, test automation specialists, developers.
**File Size**: 🟡 Medium (300 lines) - Testing for complex feature.

[← Back to Dashboard Hub](./README.md) | [← Previous: Content Strategy](./content-strategy.md) | [Next: Decisions →](./decisions.md)

---

## 🎯 Testing Objectives

### Coverage Goals
- **Unit Tests**: 85% code coverage
- **Integration Tests**: All critical user flows
- **E2E Tests**: Complete user journeys automated
- **Performance Tests**: Load testing for 10K+ concurrent users
- **Accessibility Tests**: WCAG 2.1 AA compliance
- **Security Tests**: Penetration testing and RBAC validation

### Quality Gates
```
Pre-Merge Checklist:
✓ All unit tests pass (85%+ coverage)
✓ Integration tests pass (critical flows)
✓ E2E tests pass (smoke suite)
✓ No accessibility violations (axe-core)
✓ Performance benchmarks met (<2s page load)
✓ Security scan passes (no high/critical)
✓ Load tests pass (10K concurrent users)
```

## 🧪 Test Strategy by Category

### 1. Unit Tests (85% coverage target)

#### State Management
```typescript
describe('Dashboard Store', () => {
  test('adds widget to layout', () => {
    const { result } = renderHook(() => useDashboardStore());
    act(() => result.current.addWidget(mockWidget));
    expect(result.current.layout).toHaveLength(1);
  });

  test('persists layout to localStorage', () => {
    const { result } = renderHook(() => useDashboardStore());
    act(() => {
      result.current.addWidget(mockWidget);
      result.current.updateLayout([mockWidget]);
    });

    const stored = JSON.parse(localStorage.getItem('dashboard-storage'));
    expect(stored.state.layout).toEqual([mockWidget]);
  });

  test('filters widget data by date range', () => {
    const { result } = renderHook(() => useDashboardStore());
    act(() => {
      result.current.setDateRange({
        start: '2025-01-01',
        end: '2025-01-10'
      });
    });

    expect(result.current.dateRange).toEqual({
      start: '2025-01-01',
      end: '2025-01-10'
    });
  });
});
```

#### Widget Components
```typescript
describe('MetricCard Widget', () => {
  test('displays metric value with correct formatting', () => {
    render(<MetricCard config={mockConfig} data={mockData} />);
    expect(screen.getByText('$1.2M')).toBeInTheDocument();
  });

  test('shows trend indicator based on change', () => {
    render(<MetricCard config={mockConfig} data={{ ...mockData, change: 15 }} />);
    expect(screen.getByTestId('trend-up')).toBeInTheDocument();
  });

  test('handles loading state', () => {
    render(<MetricCard config={mockConfig} isLoading={true} />);
    expect(screen.getByRole('status')).toHaveAttribute('aria-busy', 'true');
  });

  test('displays error message on failure', () => {
    render(<MetricCard config={mockConfig} error="Failed to load" />);
    expect(screen.getByRole('alert')).toHaveTextContent('Failed to load');
  });
});
```

### 2. Integration Tests (Critical Flows)

#### Real-Time Data Flow
```typescript
describe('Real-Time Data Integration', () => {
  let mockWs: MockWebSocket;

  beforeEach(() => {
    mockWs = new MockWebSocket('ws://localhost:3001');
  });

  test('connects to WebSocket and receives updates', async () => {
    render(<Dashboard />);

    await waitFor(() => {
      expect(mockWs.readyState).toBe(WebSocket.OPEN);
    });

    // Simulate metric update
    act(() => {
      mockWs.emit('metric_update', {
        widgetId: 'revenue',
        data: { value: 1300000 }
      });
    });

    await waitFor(() => {
      expect(screen.getByTestId('revenue-value')).toHaveTextContent('$1.3M');
    });
  });

  test('handles reconnection on connection loss', async () => {
    render(<Dashboard />);

    // Simulate connection loss
    act(() => mockWs.close());

    await waitFor(() => {
      expect(screen.getByText(/reconnecting/i)).toBeInTheDocument();
    });

    // Should attempt reconnect
    await waitFor(() => {
      expect(mockWs.readyState).toBe(WebSocket.OPEN);
    }, { timeout: 5000 });
  });
});
```

#### Dashboard Customization Flow
```typescript
describe('Dashboard Customization', () => {
  test('completes full customization flow', async () => {
    const user = userEvent.setup();
    render(<Dashboard />);

    // Enter edit mode
    await user.click(screen.getByRole('button', { name: /customize/i }));
    expect(screen.getByText(/edit mode/i)).toBeInTheDocument();

    // Add widget
    await user.click(screen.getByRole('button', { name: /add widget/i }));
    await user.click(screen.getByText(/conversion rate/i));
    expect(screen.getByTestId('widget-conversion-rate')).toBeInTheDocument();

    // Drag widget (simplified - actual DnD more complex)
    const widget = screen.getByTestId('widget-revenue');
    fireEvent.dragStart(widget);
    fireEvent.drop(screen.getByTestId('drop-zone-2'));

    // Exit edit mode and save
    await user.click(screen.getByRole('button', { name: /save/i }));

    await waitFor(() => {
      expect(screen.getByText(/layout saved/i)).toBeInTheDocument();
    });
  });
});
```

### 3. End-to-End Tests (Playwright)

#### Complete User Journey
```typescript
test('executive monitors dashboard and sets alert', async ({ page }) => {
  // Login
  await page.goto('/login');
  await page.fill('[name="email"]', 'exec@company.com');
  await page.fill('[name="password"]', 'password');
  await page.click('button[type="submit"]');

  // Navigate to dashboard
  await page.waitForURL('/dashboard');
  await expect(page.locator('h1')).toHaveText('Analytics Dashboard');

  // Verify widgets load
  await page.waitForSelector('[data-widget-type="metric-card"]', { timeout: 10000 });
  const widgets = await page.locator('[data-widget-type]').count();
  expect(widgets).toBeGreaterThan(0);

  // Check revenue metric
  const revenueCard = page.locator('[data-widget-id="revenue"]');
  await expect(revenueCard).toBeVisible();
  const revenueValue = await revenueCard.locator('.metric-value').textContent();
  expect(revenueValue).toMatch(/\$[\d.]+[KMB]/);

  // Set up alert
  await revenueCard.locator('[aria-label="Widget menu"]').click();
  await page.click('text=Create Alert');

  await page.fill('[name="threshold"]', '100000');
  await page.selectOption('[name="condition"]', 'below');
  await page.check('[name="notify-email"]');
  await page.click('button:has-text("Save Alert")');

  await expect(page.locator('text=Alert created')).toBeVisible();

  // Verify alert appears in alerts list
  await page.click('nav >> text=Alerts');
  await expect(page.locator('text=Revenue below $100K')).toBeVisible();
});
```

### 4. Performance Tests

#### Load Testing (k6)
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 1000 },  // Ramp up to 1K users
    { duration: '5m', target: 1000 },  // Stay at 1K for 5 min
    { duration: '2m', target: 5000 },  // Spike to 5K
    { duration: '5m', target: 5000 },  // Stay at 5K
    { duration: '2m', target: 10000 }, // Peak at 10K
    { duration: '3m', target: 10000 }, // Sustain 10K
    { duration: '2m', target: 0 },     // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests < 500ms
    http_req_failed: ['rate<0.01'],    // <1% failure rate
  },
};

export default function () {
  const response = http.get('https://api.example.com/dashboard/metrics', {
    headers: { 'Authorization': `Bearer ${__ENV.API_TOKEN}` }
  });

  check(response, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1);
}
```

#### Frontend Performance
```typescript
describe('Dashboard Performance', () => {
  test('page load time < 2 seconds', async () => {
    const startTime = performance.now();

    render(<Dashboard />);

    await waitFor(() => {
      expect(screen.getByRole('main')).toBeInTheDocument();
    });

    const loadTime = performance.now() - startTime;
    expect(loadTime).toBeLessThan(2000);
  });

  test('widget rendering < 500ms each', async () => {
    const startTime = performance.now();

    render(<MetricCard config={mockConfig} data={mockData} />);

    await waitFor(() => {
      expect(screen.getByRole('region')).toBeInTheDocument();
    });

    const renderTime = performance.now() - startTime;
    expect(renderTime).toBeLessThan(500);
  });

  test('handles 100+ data points efficiently', () => {
    const largeDataset = Array.from({ length: 100 }, (_, i) => ({
      timestamp: Date.now() - i * 1000,
      value: Math.random() * 1000
    }));

    const startTime = performance.now();
    render(<LineChart data={largeDataset} />);
    const renderTime = performance.now() - startTime;

    expect(renderTime).toBeLessThan(1000);
  });
});
```

### 5. Security Tests

#### Permission Enforcement
```typescript
describe('RBAC Security', () => {
  test('restricts widgets based on user permissions', async () => {
    const limitedUser = { role: 'viewer', permissions: ['read:revenue'] };

    render(<Dashboard user={limitedUser} />);

    // Should see revenue widget
    expect(screen.getByTestId('widget-revenue')).toBeInTheDocument();

    // Should NOT see restricted widgets
    expect(screen.queryByTestId('widget-financials')).not.toBeInTheDocument();
  });

  test('prevents unauthorized widget actions', async () => {
    const readOnlyUser = { role: 'viewer', permissions: ['read:dashboard'] };

    render(<Dashboard user={readOnlyUser} />);

    const widget = screen.getByTestId('widget-revenue');
    const menu = within(widget).getByLabelText('Widget menu');

    await userEvent.click(menu);

    // Should NOT have delete option
    expect(screen.queryByText(/remove/i)).not.toBeInTheDocument();

    // Should have view-only actions
    expect(screen.getByText(/view details/i)).toBeInTheDocument();
  });
});
```

## ♿ Accessibility Testing

```typescript
describe('Dashboard Accessibility', () => {
  test('has no axe violations', async () => {
    const { container } = render(<Dashboard />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  test('supports keyboard navigation', async () => {
    render(<Dashboard />);

    // Tab through interactive elements
    await userEvent.tab();
    expect(screen.getByRole('button', { name: /customize/i })).toHaveFocus();

    await userEvent.tab();
    expect(screen.getByRole('button', { name: /filters/i })).toHaveFocus();

    // Keyboard shortcuts
    await userEvent.keyboard('c'); // Toggle customize
    expect(screen.getByText(/edit mode/i)).toBeInTheDocument();

    await userEvent.keyboard('{Escape}'); // Exit edit mode
    expect(screen.queryByText(/edit mode/i)).not.toBeInTheDocument();
  });

  test('announces live updates to screen readers', async () => {
    render(<Dashboard />);

    const liveRegion = screen.getByRole('status');
    expect(liveRegion).toHaveAttribute('aria-live', 'polite');

    // Simulate metric update
    act(() => {
      updateMetric('revenue', { value: 1300000 });
    });

    await waitFor(() => {
      expect(liveRegion).toHaveTextContent(/revenue updated/i);
    });
  });
});
```

## 📊 Test Metrics & Reporting

### Coverage Requirements
```
Component Coverage: 85%+
Hook Coverage: 90%+
Utility Coverage: 95%+
Critical Path Coverage: 100%

Test Distribution:
- Unit: 70% of tests
- Integration: 20% of tests
- E2E: 10% of tests
```

### CI/CD Pipeline
```yaml
test-pipeline:
  - stage: unit
    run: npm test --coverage
    fail-if: coverage < 85%

  - stage: integration
    run: npm run test:integration
    fail-if: any test fails

  - stage: e2e
    run: npm run test:e2e
    fail-if: critical flows fail

  - stage: performance
    run: npm run test:perf
    fail-if: load-time > 2s OR widget-render > 500ms

  - stage: accessibility
    run: npm run test:a11y
    fail-if: any violations

  - stage: security
    run: npm run test:security
    fail-if: high/critical vulnerabilities
```

## 🔗 Related Documentation

- [Requirements](./requirements.md) - Test scenarios from requirements
- [Technical Design](./technical-design.md) - Architecture being tested
- [Implementation](./implementation.md) - Code under test
- [Decisions](./decisions.md) - Testing approach decisions

---

[← Back to Dashboard Hub](./README.md) | [← Previous: Content Strategy](./content-strategy.md) | [Next: Decisions →](./decisions.md)

**Testing Note**: This example demonstrates comprehensive testing strategy for enterprise-scale features including performance, security, and accessibility testing.

---
title: Calculator Feature - Testing Strategy
type: testing-strategy
feature: example-calculator
category: example
status: template-example
last_updated: 2025-01-10
qa_owners: ["qa-team", "engineering"]
coverage_target: 90
---

# Calculator Feature - Testing Strategy

**Purpose**: Define comprehensive testing approach and test scenarios.
**Audience**: QA engineers, developers, test automation specialists.
**File Size**: 🟢 Small (150 lines) - Focused testing specifications.

[← Back to Calculator Hub](./README.md) | [← Previous: Content Strategy](./content-strategy.md) | [Next: Decisions →](./decisions.md)

---

## 🎯 Testing Objectives

### Coverage Goals
- **Unit Tests**: 95% code coverage
- **Integration Tests**: All user flows covered
- **E2E Tests**: Critical paths automated
- **Accessibility Tests**: WCAG 2.1 AA compliance

### Quality Gates
- ✓ All unit tests pass
- ✓ No accessibility violations
- ✓ Performance under 100ms per operation
- ✓ No console errors in production build

## 🧪 Unit Test Strategy

### Pure Functions (`utils/calculator.ts`)
**Coverage Target**: 100%

```typescript
describe('calculate', () => {
  // Basic operations
  test('adds two numbers correctly', () => {
    expect(calculate(5, 3, 'add')).toBe(8);
  });

  test('subtracts two numbers correctly', () => {
    expect(calculate(10, 4, 'subtract')).toBe(6);
  });

  test('multiplies two numbers correctly', () => {
    expect(calculate(6, 7, 'multiply')).toBe(42);
  });

  test('divides two numbers correctly', () => {
    expect(calculate(15, 3, 'divide')).toBe(5);
  });

  // Edge cases
  test('throws error on division by zero', () => {
    expect(() => calculate(10, 0, 'divide'))
      .toThrow('Cannot divide by zero');
  });

  test('handles floating point precision', () => {
    expect(calculate(0.1, 0.2, 'add')).toBe(0.3);
  });

  test('handles very large numbers', () => {
    expect(calculate(1e308, 2, 'multiply')).toBe(Infinity);
  });

  test('handles very small numbers', () => {
    expect(calculate(1e-10, 1e-10, 'multiply')).toBeCloseTo(1e-20);
  });
});

describe('formatForDisplay', () => {
  test('formats normal numbers without trailing zeros', () => {
    expect(formatForDisplay(3.14000)).toBe('3.14');
  });

  test('uses exponential notation for very large numbers', () => {
    expect(formatForDisplay(1e15)).toMatch(/e\+/);
  });

  test('uses exponential notation for very small numbers', () => {
    expect(formatForDisplay(1e-10)).toMatch(/e-/);
  });
});
```

### Custom Hooks (`hooks/useCalculator.ts`)
**Coverage Target**: 90%

```typescript
describe('useCalculator', () => {
  test('initializes with display "0"', () => {
    const { result } = renderHook(() => useCalculator());
    expect(result.current.display).toBe('0');
  });

  test('handles number input', () => {
    const { result } = renderHook(() => useCalculator());
    act(() => result.current.handleNumber('5'));
    expect(result.current.display).toBe('5');
  });

  test('performs basic calculation', () => {
    const { result } = renderHook(() => useCalculator());
    act(() => {
      result.current.handleNumber('5');
      result.current.handleOperation('add');
      result.current.handleNumber('3');
      result.current.handleEquals();
    });
    expect(result.current.display).toBe('8');
  });

  test('handles clear operation', () => {
    const { result } = renderHook(() => useCalculator());
    act(() => {
      result.current.handleNumber('5');
      result.current.handleClear();
    });
    expect(result.current.display).toBe('0');
  });

  test('displays error on division by zero', () => {
    const { result } = renderHook(() => useCalculator());
    act(() => {
      result.current.handleNumber('5');
      result.current.handleOperation('divide');
      result.current.handleNumber('0');
      result.current.handleEquals();
    });
    expect(result.current.error).toBe('Cannot divide by zero');
  });
});
```

### Components
**Coverage Target**: 85%

```typescript
describe('Display', () => {
  test('renders the value correctly', () => {
    render(<Display value="42" error={null} />);
    expect(screen.getByText('42')).toBeInTheDocument();
  });

  test('renders error message when provided', () => {
    render(<Display value="0" error="Cannot divide by zero" />);
    expect(screen.getByRole('alert')).toHaveTextContent('Cannot divide by zero');
  });

  test('has proper ARIA attributes', () => {
    render(<Display value="42" error={null} />);
    const display = screen.getByRole('status');
    expect(display).toHaveAttribute('aria-live', 'polite');
  });
});

describe('Button', () => {
  test('calls onClick with correct value', () => {
    const handleClick = vi.fn();
    render(
      <Button
        value="5"
        label="5"
        onClick={handleClick}
        ariaLabel="Five"
      />
    );

    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledWith('5');
  });

  test('applies correct variant class', () => {
    render(
      <Button
        value="+"
        label="+"
        variant="operator"
        onClick={vi.fn()}
        ariaLabel="Add"
      />
    );

    expect(screen.getByRole('button')).toHaveClass('operator');
  });
});
```

## 🔄 Integration Test Strategy

### User Flow: Basic Calculation
```typescript
describe('Calculator Integration: Basic Calculation', () => {
  test('completes full calculation flow', async () => {
    render(<Calculator />);

    // Enter first number
    await userEvent.click(screen.getByLabelText('Five'));
    expect(screen.getByRole('status')).toHaveTextContent('5');

    // Select operation
    await userEvent.click(screen.getByLabelText('Add'));

    // Enter second number
    await userEvent.click(screen.getByLabelText('Three'));
    expect(screen.getByRole('status')).toHaveTextContent('3');

    // Calculate result
    await userEvent.click(screen.getByLabelText('Equals'));
    expect(screen.getByRole('status')).toHaveTextContent('8');
  });
});
```

### User Flow: Chained Operations
```typescript
test('handles chained operations', async () => {
  render(<Calculator />);

  // 5 + 3 = 8
  await userEvent.click(screen.getByLabelText('Five'));
  await userEvent.click(screen.getByLabelText('Add'));
  await userEvent.click(screen.getByLabelText('Three'));
  await userEvent.click(screen.getByLabelText('Equals'));

  // 8 × 2 = 16
  await userEvent.click(screen.getByLabelText('Multiply'));
  await userEvent.click(screen.getByLabelText('Two'));
  await userEvent.click(screen.getByLabelText('Equals'));

  expect(screen.getByRole('status')).toHaveTextContent('16');
});
```

### User Flow: Error Recovery
```typescript
test('handles error and recovery', async () => {
  render(<Calculator />);

  // Cause error: 5 ÷ 0
  await userEvent.click(screen.getByLabelText('Five'));
  await userEvent.click(screen.getByLabelText('Divide'));
  await userEvent.click(screen.getByLabelText('Zero'));
  await userEvent.click(screen.getByLabelText('Equals'));

  // Verify error displayed
  expect(screen.getByRole('alert')).toHaveTextContent('Cannot divide by zero');

  // Clear error
  await userEvent.click(screen.getByLabelText('All clear'));

  // Verify reset
  expect(screen.getByRole('status')).toHaveTextContent('0');
});
```

## ⌨️ Keyboard Interaction Tests

```typescript
describe('Keyboard Interactions', () => {
  test('handles number key input', async () => {
    render(<Calculator />);
    await userEvent.keyboard('5');
    expect(screen.getByRole('status')).toHaveTextContent('5');
  });

  test('handles operator keys', async () => {
    render(<Calculator />);
    await userEvent.keyboard('5+3=');
    expect(screen.getByRole('status')).toHaveTextContent('8');
  });

  test('handles Enter key for equals', async () => {
    render(<Calculator />);
    await userEvent.keyboard('10-4{Enter}');
    expect(screen.getByRole('status')).toHaveTextContent('6');
  });

  test('handles Escape key for clear', async () => {
    render(<Calculator />);
    await userEvent.keyboard('123{Escape}');
    expect(screen.getByRole('status')).toHaveTextContent('0');
  });

  test('prevents default browser shortcuts', async () => {
    render(<Calculator />);
    const preventDefaultSpy = vi.fn();

    // Division should prevent browser search
    fireEvent.keyDown(window, {
      key: '/',
      preventDefault: preventDefaultSpy
    });

    expect(preventDefaultSpy).toHaveBeenCalled();
  });
});
```

## ♿ Accessibility Tests

```typescript
describe('Accessibility', () => {
  test('has no accessibility violations', async () => {
    const { container } = render(<Calculator />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  test('supports keyboard navigation', async () => {
    render(<Calculator />);

    // Tab through interactive elements
    await userEvent.tab();
    expect(screen.getByLabelText('All clear')).toHaveFocus();

    await userEvent.tab();
    expect(screen.getByLabelText('Clear')).toHaveFocus();
  });

  test('announces results to screen readers', async () => {
    render(<Calculator />);
    await userEvent.click(screen.getByLabelText('Five'));
    await userEvent.click(screen.getByLabelText('Add'));
    await userEvent.click(screen.getByLabelText('Three'));
    await userEvent.click(screen.getByLabelText('Equals'));

    const status = screen.getByRole('status');
    expect(status).toHaveAttribute('aria-live', 'polite');
    expect(status).toHaveTextContent('8');
  });
});
```

## 📱 Responsive/Mobile Tests

```typescript
describe('Responsive Design', () => {
  test('renders correctly on mobile viewport', () => {
    global.innerWidth = 375;
    global.innerHeight = 667;
    fireEvent(window, new Event('resize'));

    render(<Calculator />);
    const calculator = screen.getByRole('main');
    expect(calculator).toHaveStyle({ maxWidth: '100%' });
  });

  test('handles touch interactions', async () => {
    render(<Calculator />);
    const button = screen.getByLabelText('Five');

    fireEvent.touchStart(button);
    fireEvent.touchEnd(button);

    expect(screen.getByRole('status')).toHaveTextContent('5');
  });
});
```

## 🎭 Visual Regression Tests

```typescript
describe('Visual Regression', () => {
  test('matches snapshot for default state', () => {
    const { container } = render(<Calculator />);
    expect(container).toMatchSnapshot();
  });

  test('matches snapshot for error state', async () => {
    render(<Calculator />);

    await userEvent.click(screen.getByLabelText('Five'));
    await userEvent.click(screen.getByLabelText('Divide'));
    await userEvent.click(screen.getByLabelText('Zero'));
    await userEvent.click(screen.getByLabelText('Equals'));

    expect(screen.getByRole('alert')).toMatchSnapshot();
  });
});
```

## 🚀 Performance Tests

```typescript
describe('Performance', () => {
  test('calculation completes in under 100ms', async () => {
    const start = performance.now();

    const result = calculate(999999, 888888, 'multiply');

    const duration = performance.now() - start;
    expect(duration).toBeLessThan(100);
  });

  test('handles rapid button clicks', async () => {
    render(<Calculator />);

    const clicks = Array(100).fill(null).map((_, i) =>
      userEvent.click(screen.getByLabelText('Five'))
    );

    await Promise.all(clicks);

    // Should not crash or hang
    expect(screen.getByRole('status')).toBeInTheDocument();
  });
});
```

## 🔗 Related Documentation

- [Requirements](./requirements.md) - Test scenarios from requirements
- [User Experience](./user-experience.md) - UX flows to test
- [Implementation](./implementation.md) - Code to test
- [Decisions](./decisions.md) - Testing approach decisions

---

[← Back to Calculator Hub](./README.md) | [← Previous: Content Strategy](./content-strategy.md) | [Next: Decisions →](./decisions.md)

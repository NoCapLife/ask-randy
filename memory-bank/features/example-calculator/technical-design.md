---
title: Calculator Feature - Technical Design
type: technical-design
feature: example-calculator
category: example
status: template-example
last_updated: 2025-01-10
architects: ["engineering-team"]
tech_stack: ["react", "typescript", "vitest"]
---

# Calculator Feature - Technical Design

**Purpose**: Define architecture, business logic, and technical specifications.
**Audience**: Software engineers, technical leads, architects.
**File Size**: 🟡 Medium (300 lines) - Comprehensive technical specifications.

[← Back to Calculator Hub](./README.md) | [← Previous: User Experience](./user-experience.md) | [Next: Implementation →](./implementation.md)

---

## 🏗️ Architecture Overview

### Component Architecture
```
CalculatorFeature/
├── Calculator.tsx              (Container component)
├── components/
│   ├── Display.tsx            (Result display)
│   ├── ButtonPad.tsx          (Number/operator grid)
│   ├── HistoryPanel.tsx       (Calculation history)
│   └── Button.tsx             (Reusable button)
├── hooks/
│   ├── useCalculator.ts       (Core calculation logic)
│   ├── useHistory.ts          (History management)
│   └── useKeyboard.ts         (Keyboard shortcuts)
├── utils/
│   ├── calculator.ts          (Pure calculation functions)
│   ├── formatter.ts           (Number formatting)
│   └── validator.ts           (Input validation)
└── types/
    └── calculator.types.ts    (TypeScript definitions)
```

### Component Hierarchy
```
<Calculator>
  ├── <Display value={currentValue} />
  ├── <ButtonPad onButtonClick={handleInput} />
  │   └── <Button /> (×20)
  └── <HistoryPanel
        history={history}
        onSelect={handleHistorySelect}
      />
```

## 🧮 Core Business Logic

### State Management

#### Calculator State
```typescript
interface CalculatorState {
  display: string;              // Current display value
  currentValue: number | null;  // Current operand
  previousValue: number | null; // Previous operand
  operation: Operation | null;  // Active operation
  isNewEntry: boolean;          // Ready for new number
  error: string | null;         // Error message
}

type Operation = 'add' | 'subtract' | 'multiply' | 'divide';
```

#### History State
```typescript
interface HistoryEntry {
  id: string;                   // Unique identifier
  expression: string;           // "5 + 3"
  result: number;               // 8
  timestamp: number;            // Unix timestamp
}

interface HistoryState {
  entries: HistoryEntry[];      // Max 10 entries
  isExpanded: boolean;          // Panel visibility
}
```

### Calculation Engine

#### Core Operations
```typescript
// Pure functions for calculations
const operations = {
  add: (a: number, b: number): number => a + b,
  subtract: (a: number, b: number): number => a - b,
  multiply: (a: number, b: number): number => a * b,
  divide: (a: number, b: number): number => {
    if (b === 0) {
      throw new Error('Cannot divide by zero');
    }
    return a / b;
  }
};

// Calculate with precision handling
function calculate(
  a: number,
  b: number,
  operation: Operation
): number {
  const result = operations[operation](a, b);

  // Handle precision issues
  return roundToPrecision(result, 10);
}
```

#### Precision Handling
```typescript
function roundToPrecision(value: number, precision: number): number {
  // Avoid floating-point errors
  const multiplier = Math.pow(10, precision);
  return Math.round(value * multiplier) / multiplier;
}

function formatForDisplay(value: number): string {
  // Use exponential notation for very large/small numbers
  if (Math.abs(value) >= 1e10 ||
      (Math.abs(value) < 1e-6 && value !== 0)) {
    return value.toExponential(6);
  }

  // Remove trailing zeros
  return value.toString().replace(/\.?0+$/, '');
}
```

### Input Processing

#### Number Input Handler
```typescript
function handleNumberInput(
  state: CalculatorState,
  digit: string
): CalculatorState {
  // Start new entry after operation
  if (state.isNewEntry) {
    return {
      ...state,
      display: digit,
      isNewEntry: false
    };
  }

  // Prevent multiple decimal points
  if (digit === '.' && state.display.includes('.')) {
    return state;
  }

  // Append digit to display
  return {
    ...state,
    display: state.display === '0' ? digit : state.display + digit
  };
}
```

#### Operation Input Handler
```typescript
function handleOperationInput(
  state: CalculatorState,
  operation: Operation
): CalculatorState {
  const currentValue = parseFloat(state.display);

  // Execute pending operation first
  if (state.operation && state.previousValue !== null && !state.isNewEntry) {
    const result = calculate(state.previousValue, currentValue, state.operation);

    return {
      ...state,
      display: formatForDisplay(result),
      previousValue: result,
      currentValue: null,
      operation,
      isNewEntry: true
    };
  }

  // Set up new operation
  return {
    ...state,
    previousValue: currentValue,
    operation,
    isNewEntry: true
  };
}
```

#### Equals Handler
```typescript
function handleEquals(state: CalculatorState): CalculatorState {
  if (!state.operation || state.previousValue === null) {
    return state;
  }

  const currentValue = parseFloat(state.display);

  try {
    const result = calculate(state.previousValue, currentValue, state.operation);

    // Add to history
    const historyEntry: HistoryEntry = {
      id: generateId(),
      expression: `${state.previousValue} ${getOperatorSymbol(state.operation)} ${currentValue}`,
      result,
      timestamp: Date.now()
    };

    return {
      ...state,
      display: formatForDisplay(result),
      previousValue: null,
      currentValue: result,
      operation: null,
      isNewEntry: true,
      error: null
    };
  } catch (error) {
    return {
      ...state,
      error: error.message,
      isNewEntry: true
    };
  }
}
```

### History Management

#### Add to History
```typescript
function addToHistory(
  history: HistoryEntry[],
  entry: HistoryEntry
): HistoryEntry[] {
  // Add to beginning, limit to 10
  const newHistory = [entry, ...history];
  return newHistory.slice(0, 10);
}
```

#### History Persistence
```typescript
// Save to localStorage
function saveHistory(history: HistoryEntry[]): void {
  try {
    localStorage.setItem('calculator-history', JSON.stringify(history));
  } catch (error) {
    console.error('Failed to save history:', error);
  }
}

// Load from localStorage
function loadHistory(): HistoryEntry[] {
  try {
    const saved = localStorage.getItem('calculator-history');
    return saved ? JSON.parse(saved) : [];
  } catch (error) {
    console.error('Failed to load history:', error);
    return [];
  }
}
```

## 🎯 Custom Hooks Design

### useCalculator Hook
```typescript
function useCalculator() {
  const [state, setState] = useState<CalculatorState>({
    display: '0',
    currentValue: null,
    previousValue: null,
    operation: null,
    isNewEntry: true,
    error: null
  });

  const handleNumber = useCallback((digit: string) => {
    setState(prev => handleNumberInput(prev, digit));
  }, []);

  const handleOperation = useCallback((op: Operation) => {
    setState(prev => handleOperationInput(prev, op));
  }, []);

  const handleEquals = useCallback(() => {
    setState(prev => handleEquals(prev));
  }, []);

  const handleClear = useCallback(() => {
    setState({
      display: '0',
      currentValue: null,
      previousValue: null,
      operation: null,
      isNewEntry: true,
      error: null
    });
  }, []);

  return {
    display: state.display,
    error: state.error,
    handleNumber,
    handleOperation,
    handleEquals,
    handleClear
  };
}
```

### useHistory Hook
```typescript
function useHistory() {
  const [history, setHistory] = useState<HistoryEntry[]>(() => loadHistory());
  const [isExpanded, setIsExpanded] = useState(false);

  // Save to localStorage on change
  useEffect(() => {
    saveHistory(history);
  }, [history]);

  const addEntry = useCallback((entry: HistoryEntry) => {
    setHistory(prev => addToHistory(prev, entry));
  }, []);

  const clearHistory = useCallback(() => {
    setHistory([]);
  }, []);

  const toggleExpanded = useCallback(() => {
    setIsExpanded(prev => !prev);
  }, []);

  return {
    history,
    isExpanded,
    addEntry,
    clearHistory,
    toggleExpanded
  };
}
```

### useKeyboard Hook
```typescript
function useKeyboard(handlers: KeyboardHandlers) {
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      const { key } = event;

      // Numbers
      if (/^[0-9.]$/.test(key)) {
        handlers.onNumber(key);
        event.preventDefault();
      }

      // Operators
      if (key === '+') handlers.onOperation('add');
      if (key === '-') handlers.onOperation('subtract');
      if (key === '*') handlers.onOperation('multiply');
      if (key === '/') {
        handlers.onOperation('divide');
        event.preventDefault(); // Prevent browser search
      }

      // Actions
      if (key === 'Enter') {
        handlers.onEquals();
        event.preventDefault();
      }
      if (key === 'Escape') {
        handlers.onClear();
      }
      if (key === 'Backspace') {
        handlers.onBackspace();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handlers]);
}
```

## 🔒 Input Validation

### Number Validation
```typescript
function isValidNumber(input: string): boolean {
  // Allow numbers, single decimal point, optional negative sign
  const numberRegex = /^-?\d*\.?\d*$/;

  // Check format
  if (!numberRegex.test(input)) {
    return false;
  }

  // Check range
  const value = parseFloat(input);
  if (isNaN(value)) {
    return true; // Allow partial input like "5."
  }

  return Math.abs(value) <= Number.MAX_VALUE;
}
```

### Operation Validation
```typescript
function isValidOperation(op: string): op is Operation {
  return ['add', 'subtract', 'multiply', 'divide'].includes(op);
}
```

## 🎨 Styling Architecture

### Component-Level Styles
```typescript
// Using CSS Modules or styled-components
const styles = {
  calculator: {
    display: 'grid',
    gridTemplateRows: 'auto 1fr auto',
    gap: 'var(--spacing-md)',
    padding: 'var(--spacing-lg)',
    maxWidth: '400px',
    margin: '0 auto'
  },
  display: {
    fontSize: 'var(--size-display)',
    fontFamily: 'var(--font-display)',
    textAlign: 'right',
    padding: 'var(--spacing-md)',
    backgroundColor: 'var(--display-bg)',
    borderRadius: 'var(--border-radius)',
    minHeight: '80px'
  },
  buttonPad: {
    display: 'grid',
    gridTemplateColumns: 'repeat(4, 1fr)',
    gap: 'var(--button-gap)'
  }
};
```

## 📊 Performance Considerations

### Optimization Strategies
1. **Memoization**: Use `useMemo` for expensive calculations
2. **Callback stability**: Use `useCallback` for event handlers
3. **Lazy loading**: History panel loads on first expansion
4. **Debouncing**: Keyboard input debounced by 50ms
5. **Virtual rendering**: History list uses virtual scrolling for 100+ items

### Bundle Size Optimization
- No external calculation libraries
- Tree-shaking for unused utilities
- Dynamic import for history panel
- Estimated bundle size: ~15KB (gzipped)

## 🧪 Testing Strategy

### Unit Tests
- Pure calculation functions (100% coverage)
- State reducers and handlers
- Validation functions
- Formatting utilities

### Integration Tests
- Component interactions
- Hook behavior
- Keyboard shortcuts
- History persistence

### Edge Case Testing
- Division by zero
- Very large/small numbers
- Rapid button clicks
- Invalid input sequences

## 🔗 Related Documentation

- [Requirements](./requirements.md) - Business requirements
- [User Experience](./user-experience.md) - UX specifications
- [Implementation](./implementation.md) - Step-by-step build guide
- [Testing Strategy](./testing-strategy.md) - Test scenarios

---

[← Back to Calculator Hub](./README.md) | [← Previous: User Experience](./user-experience.md) | [Next: Implementation →](./implementation.md)

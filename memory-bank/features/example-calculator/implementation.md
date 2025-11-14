---
title: Calculator Feature - Implementation Guide
type: implementation
feature: example-calculator
category: example
status: template-example
last_updated: 2025-01-10
developers: ["engineering-team"]
estimated_hours: 6
---

# Calculator Feature - Implementation Guide

**Purpose**: Step-by-step implementation instructions with code examples.
**Audience**: Software engineers implementing the feature.
**File Size**: 🟡 Medium (400 lines) - Detailed implementation walkthrough.

[← Back to Calculator Hub](./README.md) | [← Previous: Technical Design](./technical-design.md) | [Next: Content Strategy →](./content-strategy.md)

---

## 📋 Implementation Checklist

### Phase 1: Foundation (2 hours)
- [ ] Set up component structure
- [ ] Create TypeScript types
- [ ] Implement pure calculation functions
- [ ] Write unit tests for calculations

### Phase 2: Core Components (2 hours)
- [ ] Build Display component
- [ ] Build ButtonPad component
- [ ] Build Button component
- [ ] Implement basic styling

### Phase 3: State Management (1 hour)
- [ ] Implement useCalculator hook
- [ ] Add keyboard support with useKeyboard hook
- [ ] Connect components to state

### Phase 4: History Feature (1 hour)
- [ ] Build HistoryPanel component
- [ ] Implement useHistory hook
- [ ] Add localStorage persistence
- [ ] Add history interactions

### Phase 5: Testing & Polish (1 hour)
- [ ] Write component tests
- [ ] Add accessibility features
- [ ] Implement error handling
- [ ] Performance optimization

---

## 🔧 Step-by-Step Implementation

### Step 1: Set Up TypeScript Types

**File**: `types/calculator.types.ts`

```typescript
// Core types
export type Operation = 'add' | 'subtract' | 'multiply' | 'divide';

export interface CalculatorState {
  display: string;
  currentValue: number | null;
  previousValue: number | null;
  operation: Operation | null;
  isNewEntry: boolean;
  error: string | null;
}

export interface HistoryEntry {
  id: string;
  expression: string;
  result: number;
  timestamp: number;
}

export interface ButtonConfig {
  value: string;
  label: string;
  type: 'number' | 'operation' | 'action';
  variant?: 'primary' | 'operator' | 'clear';
  gridColumn?: string;
  ariaLabel: string;
}

// Event handlers
export interface CalculatorHandlers {
  onNumber: (digit: string) => void;
  onOperation: (op: Operation) => void;
  onEquals: () => void;
  onClear: () => void;
  onClearAll: () => void;
  onBackspace: () => void;
}
```

### Step 2: Create Pure Calculation Functions

**File**: `utils/calculator.ts`

```typescript
import { Operation } from '../types/calculator.types';

// Core operations
const operations: Record<Operation, (a: number, b: number) => number> = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
  divide: (a, b) => {
    if (b === 0) {
      throw new Error('Cannot divide by zero');
    }
    return a / b;
  }
};

// Main calculation function
export function calculate(
  a: number,
  b: number,
  operation: Operation
): number {
  const result = operations[operation](a, b);
  return roundToPrecision(result, 10);
}

// Precision handling
export function roundToPrecision(value: number, precision: number): number {
  const multiplier = Math.pow(10, precision);
  return Math.round(value * multiplier) / multiplier;
}

// Number formatting
export function formatForDisplay(value: number): string {
  // Exponential notation for very large/small numbers
  if (Math.abs(value) >= 1e10 || (Math.abs(value) < 1e-6 && value !== 0)) {
    return value.toExponential(6);
  }

  // Remove trailing zeros
  return value.toString().replace(/\.?0+$/, '');
}

// Operator symbol conversion
export function getOperatorSymbol(operation: Operation): string {
  const symbols: Record<Operation, string> = {
    add: '+',
    subtract: '-',
    multiply: '×',
    divide: '÷'
  };
  return symbols[operation];
}

// Input validation
export function isValidNumber(input: string): boolean {
  const numberRegex = /^-?\d*\.?\d*$/;
  if (!numberRegex.test(input)) return false;

  const value = parseFloat(input);
  if (isNaN(value)) return true; // Allow partial input

  return Math.abs(value) <= Number.MAX_VALUE;
}
```

**Tests**: `utils/__tests__/calculator.test.ts`

```typescript
import { describe, it, expect } from 'vitest';
import { calculate, formatForDisplay, roundToPrecision } from '../calculator';

describe('calculate', () => {
  it('should add two numbers', () => {
    expect(calculate(5, 3, 'add')).toBe(8);
  });

  it('should subtract two numbers', () => {
    expect(calculate(10, 4, 'subtract')).toBe(6);
  });

  it('should multiply two numbers', () => {
    expect(calculate(6, 7, 'multiply')).toBe(42);
  });

  it('should divide two numbers', () => {
    expect(calculate(15, 3, 'divide')).toBe(5);
  });

  it('should throw error on division by zero', () => {
    expect(() => calculate(10, 0, 'divide')).toThrow('Cannot divide by zero');
  });

  it('should handle floating point precision', () => {
    expect(calculate(0.1, 0.2, 'add')).toBe(0.3);
  });
});

describe('formatForDisplay', () => {
  it('should format normal numbers', () => {
    expect(formatForDisplay(42)).toBe('42');
  });

  it('should remove trailing zeros', () => {
    expect(formatForDisplay(3.1400)).toBe('3.14');
  });

  it('should use exponential for very large numbers', () => {
    expect(formatForDisplay(1e15)).toBe('1.000000e+15');
  });
});
```

### Step 3: Implement useCalculator Hook

**File**: `hooks/useCalculator.ts`

```typescript
import { useState, useCallback } from 'react';
import { CalculatorState, Operation } from '../types/calculator.types';
import { calculate, formatForDisplay } from '../utils/calculator';

const initialState: CalculatorState = {
  display: '0',
  currentValue: null,
  previousValue: null,
  operation: null,
  isNewEntry: true,
  error: null
};

export function useCalculator() {
  const [state, setState] = useState<CalculatorState>(initialState);

  const handleNumber = useCallback((digit: string) => {
    setState(prev => {
      // Clear error
      if (prev.error) {
        return { ...initialState, display: digit, isNewEntry: false };
      }

      // Start new entry after operation
      if (prev.isNewEntry) {
        return { ...prev, display: digit, isNewEntry: false };
      }

      // Prevent multiple decimal points
      if (digit === '.' && prev.display.includes('.')) {
        return prev;
      }

      // Append digit
      const newDisplay = prev.display === '0' && digit !== '.'
        ? digit
        : prev.display + digit;

      return { ...prev, display: newDisplay };
    });
  }, []);

  const handleOperation = useCallback((operation: Operation) => {
    setState(prev => {
      if (prev.error) return initialState;

      const currentValue = parseFloat(prev.display);

      // Execute pending operation
      if (prev.operation && prev.previousValue !== null && !prev.isNewEntry) {
        try {
          const result = calculate(prev.previousValue, currentValue, prev.operation);
          return {
            ...prev,
            display: formatForDisplay(result),
            previousValue: result,
            operation,
            isNewEntry: true,
            error: null
          };
        } catch (error) {
          return { ...prev, error: (error as Error).message, isNewEntry: true };
        }
      }

      // Set up new operation
      return {
        ...prev,
        previousValue: currentValue,
        operation,
        isNewEntry: true
      };
    });
  }, []);

  const handleEquals = useCallback(() => {
    setState(prev => {
      if (prev.error) return initialState;
      if (!prev.operation || prev.previousValue === null) return prev;

      const currentValue = parseFloat(prev.display);

      try {
        const result = calculate(prev.previousValue, currentValue, prev.operation);
        return {
          ...prev,
          display: formatForDisplay(result),
          previousValue: null,
          currentValue: result,
          operation: null,
          isNewEntry: true,
          error: null
        };
      } catch (error) {
        return { ...prev, error: (error as Error).message, isNewEntry: true };
      }
    });
  }, []);

  const handleClear = useCallback(() => {
    setState(prev => ({ ...prev, display: '0', isNewEntry: true, error: null }));
  }, []);

  const handleClearAll = useCallback(() => {
    setState(initialState);
  }, []);

  const handleBackspace = useCallback(() => {
    setState(prev => {
      if (prev.error || prev.isNewEntry) return prev;

      const newDisplay = prev.display.length > 1
        ? prev.display.slice(0, -1)
        : '0';

      return { ...prev, display: newDisplay };
    });
  }, []);

  return {
    display: state.display,
    error: state.error,
    operation: state.operation,
    handleNumber,
    handleOperation,
    handleEquals,
    handleClear,
    handleClearAll,
    handleBackspace
  };
}
```

### Step 4: Build Display Component

**File**: `components/Display.tsx`

```typescript
import React from 'react';
import styles from './Display.module.css';

interface DisplayProps {
  value: string;
  error: string | null;
}

export function Display({ value, error }: DisplayProps) {
  return (
    <div className={styles.display}>
      <div
        className={styles.value}
        role="status"
        aria-live="polite"
        aria-atomic="true"
      >
        {error ? (
          <span className={styles.error} role="alert">
            {error}
          </span>
        ) : (
          value
        )}
      </div>
    </div>
  );
}
```

**Styles**: `components/Display.module.css`

```css
.display {
  background-color: var(--display-bg);
  border-radius: var(--border-radius);
  padding: var(--spacing-md);
  min-height: 80px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.value {
  font-family: var(--font-display);
  font-size: var(--size-display);
  color: var(--display-text);
  font-weight: var(--weight-medium);
  word-break: break-all;
  text-align: right;
}

.error {
  color: var(--error-color);
  font-size: 18px;
  animation: shake 0.5s ease-in-out;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-10px); }
  75% { transform: translateX(10px); }
}
```

### Step 5: Build Button Component

**File**: `components/Button.tsx`

```typescript
import React from 'react';
import styles from './Button.module.css';

interface ButtonProps {
  value: string;
  label: string;
  variant?: 'primary' | 'operator' | 'clear';
  onClick: (value: string) => void;
  ariaLabel: string;
  gridColumn?: string;
}

export function Button({
  value,
  label,
  variant = 'primary',
  onClick,
  ariaLabel,
  gridColumn
}: ButtonProps) {
  return (
    <button
      className={`${styles.button} ${styles[variant]}`}
      style={{ gridColumn }}
      onClick={() => onClick(value)}
      aria-label={ariaLabel}
      type="button"
    >
      {label}
    </button>
  );
}
```

**Styles**: `components/Button.module.css`

```css
.button {
  font-family: var(--font-button);
  font-size: var(--size-button);
  font-weight: var(--weight-medium);
  border: none;
  border-radius: var(--border-radius);
  padding: var(--spacing-md);
  min-height: 60px;
  cursor: pointer;
  transition: all 150ms ease-out;
  user-select: none;
}

.button:hover {
  transform: scale(1.02);
  opacity: 0.9;
}

.button:active {
  transform: scale(0.98);
}

.button:focus-visible {
  outline: 2px solid var(--button-primary);
  outline-offset: 2px;
}

.primary {
  background-color: var(--button-number);
  color: var(--button-text);
}

.operator {
  background-color: var(--button-operator);
  color: white;
}

.clear {
  background-color: var(--button-clear);
  color: white;
}

@media (max-width: 768px) {
  .button {
    min-height: 50px;
    font-size: 20px;
  }
}
```

### Step 6: Build ButtonPad Component

**File**: `components/ButtonPad.tsx`

```typescript
import React from 'react';
import { Button } from './Button';
import { ButtonConfig } from '../types/calculator.types';
import styles from './ButtonPad.module.css';

interface ButtonPadProps {
  onButtonClick: (value: string, type: string) => void;
}

const buttonLayout: ButtonConfig[] = [
  { value: 'AC', label: 'AC', type: 'action', variant: 'clear', ariaLabel: 'All clear' },
  { value: 'C', label: 'C', type: 'action', variant: 'clear', ariaLabel: 'Clear' },
  { value: '%', label: '%', type: 'operation', variant: 'operator', ariaLabel: 'Percent' },
  { value: 'divide', label: '÷', type: 'operation', variant: 'operator', ariaLabel: 'Divide' },

  { value: '7', label: '7', type: 'number', ariaLabel: 'Seven' },
  { value: '8', label: '8', type: 'number', ariaLabel: 'Eight' },
  { value: '9', label: '9', type: 'number', ariaLabel: 'Nine' },
  { value: 'multiply', label: '×', type: 'operation', variant: 'operator', ariaLabel: 'Multiply' },

  { value: '4', label: '4', type: 'number', ariaLabel: 'Four' },
  { value: '5', label: '5', type: 'number', ariaLabel: 'Five' },
  { value: '6', label: '6', type: 'number', ariaLabel: 'Six' },
  { value: 'subtract', label: '-', type: 'operation', variant: 'operator', ariaLabel: 'Subtract' },

  { value: '1', label: '1', type: 'number', ariaLabel: 'One' },
  { value: '2', label: '2', type: 'number', ariaLabel: 'Two' },
  { value: '3', label: '3', type: 'number', ariaLabel: 'Three' },
  { value: 'add', label: '+', type: 'operation', variant: 'operator', ariaLabel: 'Add' },

  { value: '0', label: '0', type: 'number', gridColumn: '1 / 3', ariaLabel: 'Zero' },
  { value: '.', label: '.', type: 'number', ariaLabel: 'Decimal point' },
  { value: '=', label: '=', type: 'action', variant: 'operator', ariaLabel: 'Equals' }
];

export function ButtonPad({ onButtonClick }: ButtonPadProps) {
  return (
    <div className={styles.buttonPad} role="group" aria-label="Calculator buttons">
      {buttonLayout.map((config) => (
        <Button
          key={config.value}
          value={config.value}
          label={config.label}
          variant={config.variant}
          onClick={(value) => onButtonClick(value, config.type)}
          ariaLabel={config.ariaLabel}
          gridColumn={config.gridColumn}
        />
      ))}
    </div>
  );
}
```

**Styles**: `components/ButtonPad.module.css`

```css
.buttonPad {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--button-gap);
}
```

### Step 7: Implement Main Calculator Component

**File**: `Calculator.tsx`

```typescript
import React from 'react';
import { Display } from './components/Display';
import { ButtonPad } from './components/ButtonPad';
import { useCalculator } from './hooks/useCalculator';
import { useKeyboard } from './hooks/useKeyboard';
import { Operation } from './types/calculator.types';
import styles from './Calculator.module.css';

export function Calculator() {
  const {
    display,
    error,
    handleNumber,
    handleOperation,
    handleEquals,
    handleClear,
    handleClearAll,
    handleBackspace
  } = useCalculator();

  // Keyboard support
  useKeyboard({
    onNumber: handleNumber,
    onOperation: handleOperation,
    onEquals: handleEquals,
    onClear: handleClearAll,
    onBackspace: handleBackspace
  });

  const handleButtonClick = (value: string, type: string) => {
    if (type === 'number') {
      handleNumber(value);
    } else if (type === 'operation') {
      handleOperation(value as Operation);
    } else if (value === 'AC') {
      handleClearAll();
    } else if (value === 'C') {
      handleClear();
    } else if (value === '=') {
      handleEquals();
    }
  };

  return (
    <div className={styles.calculator}>
      <header className={styles.header}>
        <h1>Calculator</h1>
      </header>

      <Display value={display} error={error} />
      <ButtonPad onButtonClick={handleButtonClick} />
    </div>
  );
}
```

### Step 8: Add Keyboard Support Hook

**File**: `hooks/useKeyboard.ts`

```typescript
import { useEffect } from 'react';
import { Operation } from '../types/calculator.types';

interface KeyboardHandlers {
  onNumber: (digit: string) => void;
  onOperation: (op: Operation) => void;
  onEquals: () => void;
  onClear: () => void;
  onBackspace: () => void;
}

export function useKeyboard(handlers: KeyboardHandlers) {
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      const { key } = event;

      // Numbers and decimal
      if (/^[0-9.]$/.test(key)) {
        handlers.onNumber(key);
        event.preventDefault();
      }

      // Operations
      const operationMap: Record<string, Operation> = {
        '+': 'add',
        '-': 'subtract',
        '*': 'multiply',
        '/': 'divide'
      };

      if (key in operationMap) {
        handlers.onOperation(operationMap[key]);
        event.preventDefault();
      }

      // Actions
      if (key === 'Enter' || key === '=') {
        handlers.onEquals();
        event.preventDefault();
      }

      if (key === 'Escape') {
        handlers.onClear();
        event.preventDefault();
      }

      if (key === 'Backspace') {
        handlers.onBackspace();
        event.preventDefault();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handlers]);
}
```

## 🔗 Related Documentation

- [Requirements](./requirements.md) - Feature requirements
- [Technical Design](./technical-design.md) - Architecture details
- [Content Strategy](./content-strategy.md) - UI copy and messages
- [Testing Strategy](./testing-strategy.md) - Testing approach

---

[← Back to Calculator Hub](./README.md) | [← Previous: Technical Design](./technical-design.md) | [Next: Content Strategy →](./content-strategy.md)

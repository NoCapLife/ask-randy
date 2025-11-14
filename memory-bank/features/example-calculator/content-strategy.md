---
title: Calculator Feature - Content Strategy
type: content-strategy
feature: example-calculator
category: example
status: template-example
last_updated: 2025-01-10
content_owners: ["ux-team", "copywriting"]
---

# Calculator Feature - Content Strategy

**Purpose**: Define all UI copy, error messages, and accessibility labels.
**Audience**: UX writers, designers, accessibility specialists.
**File Size**: 🟡 Medium (200 lines) - Comprehensive content specifications.

[← Back to Calculator Hub](./README.md) | [← Previous: Implementation](./implementation.md) | [Next: Testing Strategy →](./testing-strategy.md)

---

## 📝 Content Principles

### Voice & Tone
- **Voice**: Clear, concise, helpful
- **Tone**: Professional yet friendly
- **Style**: Plain language, avoid jargon
- **Personality**: Reliable calculator assistant

### Writing Guidelines
1. Use simple, direct language
2. Provide context for errors
3. Offer clear next steps
4. Be consistent across all messages
5. Prioritize accessibility

## 🔤 UI Copy

### Header & Navigation
```
Header Title: "Calculator"
Help Button: "?" (aria-label: "Calculator help")
History Toggle: "History" (aria-label: "Show calculation history")
```

### Button Labels
```
Numbers:
- "0" through "9" (aria-label: "Zero" through "Nine")
- "." (label: ".", aria-label: "Decimal point")

Operations:
- "+" (label: "+", aria-label: "Add")
- "-" (label: "-", aria-label: "Subtract")
- "×" (label: "×", aria-label: "Multiply")
- "÷" (label: "÷", aria-label: "Divide")

Actions:
- "=" (label: "=", aria-label: "Equals")
- "C" (label: "C", aria-label: "Clear current entry")
- "AC" (label: "AC", aria-label: "All clear - reset calculator")
- "%" (label: "%", aria-label: "Percent")
```

### Display Area
```
Default: "0"
Empty State (aria-label): "Calculator ready for input"
Result State (aria-label): "Result: [value]"
Operation State (aria-label): "[previous] [operator] [current]"
```

## ⚠️ Error Messages

### Division by Zero
```
Display: "Error: Cannot divide by zero"
Screen Reader: "Error: Cannot divide by zero. Press all clear to reset."
Recovery: Show AC button prominently
Next Steps: "Press AC to clear and start a new calculation"
```

### Number Too Large
```
Display: "Error: Number too large"
Screen Reader: "Error: Result exceeds maximum value. Press all clear to reset."
Recovery: Auto-convert to exponential notation if possible
Fallback: Show error and require AC
```

### Invalid Input
```
Display: "Error: Invalid input"
Screen Reader: "Error: Invalid input detected. Press all clear to reset."
Context: "Only numbers and basic operators are allowed"
```

### Calculation Error
```
Display: "Error: Calculation failed"
Screen Reader: "Error: Unable to complete calculation. Press all clear to reset."
Debug Info: (Logged to console, not shown to user)
```

## ♿ Accessibility Labels

### ARIA Live Regions
```html
<!-- Display announces changes -->
<div role="status" aria-live="polite" aria-atomic="true">
  Result: 42
</div>

<!-- Errors announce immediately -->
<div role="alert" aria-live="assertive">
  Error: Cannot divide by zero
</div>

<!-- History updates politely -->
<div role="log" aria-live="polite">
  Added to history: 5 + 3 = 8
</div>
```

### Button Accessibility
```html
<!-- Number buttons -->
<button aria-label="Five">5</button>

<!-- Operation buttons with state -->
<button
  aria-label="Add"
  aria-pressed="true"
  aria-describedby="operation-help"
>+</button>

<!-- Clear buttons with clear intent -->
<button aria-label="Clear current entry">C</button>
<button aria-label="All clear - reset calculator completely">AC</button>
```

### Screen Reader Announcements

#### Number Entry
```
User presses "5":
→ Announce: "Five"

User presses "3":
→ Announce: "Three"

Display shows "53":
→ Announce: "Fifty-three"
```

#### Operation Selection
```
User presses "+":
→ Announce: "Plus"
→ Status: "Five plus"

User presses "3":
→ Announce: "Three"

User presses "=":
→ Announce: "Equals"
→ Status: "Result: Eight"
```

#### Error States
```
Division by zero attempted:
→ Announce: "Error: Cannot divide by zero"
→ Announce: "Press all clear to reset"
→ Focus moved to AC button
```

## 📱 Mobile-Specific Copy

### Touch Interactions
```
Long-press number: "Hold for more options" (future feature)
Swipe up: "Swipe up to view history"
Swipe down: "Swipe down to close history"
```

### Haptic Feedback Labels
```
Number press: "Number entered"
Operation press: "Operation selected"
Equals press: "Calculation complete"
Error state: "Error occurred"
```

## 📊 History Panel Copy

### Header
```
Title: "History"
Clear Button: "Clear History" (aria-label: "Clear all calculation history")
Empty State: "No calculations yet"
```

### History Items
```
Format: "[expression] = [result]"
Example: "5 + 3 = 8"
Timestamp: "2 minutes ago" (aria-label: "Calculated 2 minutes ago")
```

### Empty State
```
Icon: Calculator icon
Message: "No calculations yet"
Subtext: "Your recent calculations will appear here"
```

### Clear Confirmation
```
Title: "Clear History?"
Message: "This will permanently delete all calculation history."
Cancel: "Cancel"
Confirm: "Clear History"
```

## 🔔 Toast Notifications

### History Actions
```
Added to History:
→ "Calculation saved to history"
→ Duration: 2 seconds
→ Position: Bottom center

History Cleared:
→ "History cleared"
→ Duration: 2 seconds
→ Position: Bottom center

History Restored:
→ "Calculation restored"
→ Duration: 2 seconds
→ Position: Bottom center
```

## 📚 Help Content

### Help Dialog
```
Title: "Calculator Help"

Keyboard Shortcuts:
- "0-9: Enter numbers"
- "+-*/: Basic operations"
- "Enter or =: Calculate result"
- "Escape: Clear all"
- "Backspace: Delete last digit"

Tips:
- "Click any history item to restore that calculation"
- "Use keyboard shortcuts for faster calculations"
- "Results are automatically saved to history"
```

### Tooltips
```
Display area: "Your calculation appears here"
History button: "View your recent calculations"
Clear button: "Clear current entry"
All Clear button: "Reset calculator completely"
```

## 🌍 Internationalization (i18n)

### Translation Keys
```json
{
  "calculator.title": "Calculator",
  "calculator.display.ready": "Calculator ready for input",
  "calculator.display.result": "Result: {value}",

  "calculator.button.add": "Add",
  "calculator.button.subtract": "Subtract",
  "calculator.button.multiply": "Multiply",
  "calculator.button.divide": "Divide",
  "calculator.button.equals": "Equals",
  "calculator.button.clear": "Clear current entry",
  "calculator.button.clearAll": "All clear - reset calculator",

  "calculator.error.divisionByZero": "Error: Cannot divide by zero",
  "calculator.error.numberTooLarge": "Error: Number too large",
  "calculator.error.invalidInput": "Error: Invalid input",

  "calculator.history.title": "History",
  "calculator.history.empty": "No calculations yet",
  "calculator.history.clear": "Clear History",
  "calculator.history.confirmClear": "This will permanently delete all calculation history.",

  "calculator.help.title": "Calculator Help",
  "calculator.help.keyboardShortcuts": "Keyboard Shortcuts"
}
```

### Number Formatting by Locale
```typescript
// en-US: 1,234.56
// fr-FR: 1 234,56
// de-DE: 1.234,56

const formatNumber = (value: number, locale: string) => {
  return new Intl.NumberFormat(locale, {
    maximumFractionDigits: 10
  }).format(value);
};
```

## 📖 Microcopy Guidelines

### Error Recovery Guidance
Always provide:
1. **What happened**: Clear error description
2. **Why it happened**: Context if helpful
3. **What to do next**: Clear action to recover

### Example Error Messages
```
❌ Bad: "Error"
✅ Good: "Error: Cannot divide by zero"

❌ Bad: "Invalid"
✅ Good: "Error: Invalid input. Only numbers and basic operators allowed."

❌ Bad: "Oops!"
✅ Good: "Error: Calculation failed. Press AC to reset."
```

### Success States
```
Calculation Complete: (Silent - result speaks for itself)
History Saved: "Saved to history" (subtle, non-intrusive)
History Restored: "Calculation restored"
```

## 🔗 Related Documentation

- [Requirements](./requirements.md) - Content requirements and user stories
- [User Experience](./user-experience.md) - UX flows and interactions
- [Testing Strategy](./testing-strategy.md) - Content validation tests

---

[← Back to Calculator Hub](./README.md) | [← Previous: Implementation](./implementation.md) | [Next: Testing Strategy →](./testing-strategy.md)

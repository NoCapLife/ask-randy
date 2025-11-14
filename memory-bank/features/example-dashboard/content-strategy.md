---
title: Dashboard Feature - Content Strategy
type: content-strategy
feature: example-dashboard
category: example
status: template-example
last_updated: 2025-01-10
content_owners: ["ux-team", "copywriting"]
---

# Dashboard Feature - Content Strategy

**Purpose**: UI copy, error messages, help content for enterprise dashboard.
**Audience**: UX writers, content strategists, accessibility specialists.
**File Size**: 🔴 Large (500 lines) - Extensive content for complex feature.

[← Back to Dashboard Hub](./README.md) | [← Previous: Implementation](./implementation.md) | [Next: Testing Strategy →](./testing-strategy.md)

---

## 📝 Content Principles

### Voice & Tone
- **Voice**: Professional, data-focused, empowering
- **Tone**: Confident but helpful, technical where appropriate
- **Style**: Clear, actionable, jargon-free for non-technical users
- **Personality**: Your trusted analytics partner

### Content Hierarchy
1. **Critical**: Errors, alerts, data loss warnings
2. **Important**: Feature guidance, incomplete data notices
3. **Helpful**: Tooltips, contextual help, onboarding
4. **Supplementary**: Keyboard shortcuts, advanced tips

## 🔤 UI Copy

### Navigation & Headers
```
Main Header: "Analytics Dashboard"
Sections:
- "Overview" → Your key metrics at a glance
- "Reports" → Detailed analysis and insights
- "Alerts" → Set up and manage notifications
- "Settings" → Customize your dashboard

Actions:
- "Customize Dashboard" → Rearrange and personalize
- "Add Widget" → Expand your dashboard
- "Share Dashboard" → Collaborate with your team
- "Export Data" → Download as PDF or CSV
```

### Widget Empty States
```
No Data Available:
Title: "No data to display"
Message: "Data will appear here once it becomes available for your selected date range."
Action: "Adjust Filters" or "Refresh Data"

No Permission:
Title: "Access restricted"
Message: "You don't have permission to view this data. Contact your administrator to request access."
Action: "Learn More" → Opens permissions help

Loading State:
Message: "Loading your metrics..."
Subtext: "This usually takes just a few seconds"

First Time Setup:
Title: "Welcome to your dashboard!"
Message: "Start by adding widgets to track your most important metrics."
Action: "Add Your First Widget"
```

### Widget Menu Actions
```
Widget Actions (accessible via ⋮ menu):
- "Refresh" → Update this widget
- "View Details" → See full data breakdown
- "Create Alert" → Get notified of changes
- "Export Data" → Download widget data
- "Duplicate Widget" → Add another instance
- "Remove" → Delete this widget (with confirmation)
```

## ⚠️ Error Messages & Recovery

### Connection Errors
```
WebSocket Disconnected:
Banner: "Live updates paused"
Message: "Connection lost. Attempting to reconnect..."
Recovery: "Reconnecting in [X] seconds" (with retry count)
Fallback: "View last known data | Refresh manually"

WebSocket Failed (after max retries):
Banner: "Live updates unavailable"
Message: "Unable to establish connection for real-time updates. Data will refresh every 60 seconds."
Action: "Try Reconnecting" or "Continue with Auto-Refresh"
```

### Data Errors
```
API Error:
Title: "Failed to load data"
Message: "We couldn't fetch your metrics. This might be a temporary issue."
Actions: "Retry" | "Report Issue" | "View Cached Data"

Partial Data:
Warning Banner: "Incomplete data"
Message: "Some metrics couldn't be loaded. Showing available data."
Details: "Missing: Revenue data, User metrics (click to retry)"

Stale Data Warning:
Indicator: "⚠️ Data may be out of date"
Tooltip: "Last updated: [timestamp]. Latest data unavailable."
Action: "Refresh Now"

Rate Limit:
Title: "Too many requests"
Message: "You've reached the limit for data requests. Please wait before refreshing."
Countdown: "You can retry in [X] seconds"
```

### User Action Errors
```
Save Layout Failed:
Toast: "Failed to save layout changes"
Message: "Your dashboard customization couldn't be saved. Try again or refresh the page."
Actions: "Retry" | "Discard Changes" | "Report Issue"

Add Widget Failed:
Message: "Couldn't add widget. You may have reached the maximum of 12 widgets."
Guidance: "Remove a widget to add a new one, or upgrade your plan for more."

Invalid Date Range:
Inline Error: "Invalid date selection"
Message: "End date must be after start date. Please adjust your selection."
Highlight: Red outline on invalid input

Alert Setup Failed:
Message: "Failed to create alert. Check your settings and try again."
Common Issues:
- "Threshold value must be a number"
- "Please select at least one notification channel"
- "Alert name already exists"
```

## 📊 Metric Explanations & Help

### Metric Tooltips (Hover States)
```
Revenue:
"Total revenue from all sources during the selected period. Includes sales, subscriptions, and one-time payments."

Monthly Recurring Revenue (MRR):
"Predictable revenue from subscriptions that recurs every month. Excludes one-time payments."

Conversion Rate:
"Percentage of visitors who completed a desired action (e.g., purchase, sign-up) during the selected period."

Churn Rate:
"Percentage of customers who cancelled or didn't renew subscriptions during the selected period."

Average Order Value (AOV):
"Average amount spent per transaction. Calculated as total revenue ÷ number of orders."
```

### Help Panel Content
```
Dashboard Help:

## Getting Started
1. Customize your dashboard by clicking "Customize Dashboard"
2. Add widgets from the widget library
3. Drag and drop to rearrange
4. Set date ranges to analyze specific time periods

## Keyboard Shortcuts
- `F` - Open filters panel
- `C` - Customize layout (toggle edit mode)
- `D` - Change date range
- `/` - Search widgets
- `?` - Show this help

## Widget Types
### Metric Cards
Display key performance indicators with trend comparisons.

### Charts
Visualize trends over time with line, bar, or pie charts.

### Data Tables
View detailed, sortable data with export options.

## Tips & Tricks
- Click any chart data point to drill down into details
- Use "Compare to previous period" for trend analysis
- Set up alerts to monitor important thresholds
- Share dashboards with your team for collaboration

Need more help? [Contact Support] or [View Documentation]
```

## 🔔 Notification Messages

### Real-Time Alerts
```
Threshold Alert (Critical):
Title: "🚨 Revenue Alert"
Message: "Revenue dropped below $100K (currently $92K)"
Time: "2 minutes ago"
Actions: "View Dashboard" | "Snooze" | "Dismiss"

Threshold Alert (Warning):
Title: "⚠️ Conversion Rate Alert"
Message: "Conversion rate decreased to 2.1% (threshold: 2.5%)"
Actions: "View Details" | "Adjust Threshold" | "Dismiss"

Data Anomaly Detection:
Title: "📊 Unusual Activity Detected"
Message: "Page views increased by 340% vs yesterday"
Context: "This may indicate a spike in traffic or a data issue"
Actions: "Investigate" | "Mark as Expected" | "Dismiss"
```

### System Notifications
```
Dashboard Shared:
Toast: "Dashboard shared with team@company.com"
Duration: 3 seconds

Export Complete:
Toast: "Report exported successfully"
Action: "Download" (opens file)

Layout Saved:
Toast: "Layout saved"
Duration: 2 seconds (auto-dismiss)

Data Refreshed:
Subtle indicator: "Updated just now" (in widget footer)
```

## ♿ Accessibility Labels & Announcements

### ARIA Labels
```html
<!-- Widget Container -->
<section
  role="region"
  aria-label="Revenue metric widget"
  aria-describedby="revenue-description"
>
  <h2 id="revenue-heading">Total Revenue</h2>
  <div id="revenue-description" class="sr-only">
    Current value: $1.2 million. Up 15% from previous period.
    Chart shows trend over last 7 days.
  </div>
</section>

<!-- Interactive Chart -->
<div
  role="img"
  aria-label="Revenue trend chart showing growth from $1 million to $1.2 million over the past 7 days"
  tabindex="0"
>
  <svg><!-- Chart visualization --></svg>
</div>

<!-- Alert Status -->
<div
  role="status"
  aria-live="polite"
  aria-atomic="true"
  class="sr-only"
>
  Alert triggered: Revenue below threshold
</div>

<!-- Edit Mode -->
<div
  role="region"
  aria-label="Dashboard edit mode active"
  aria-live="assertive"
>
  Edit mode: Drag widgets to rearrange. Press Escape to exit.
</div>
```

### Screen Reader Announcements
```
Dashboard Load Complete:
→ "Dashboard loaded. Showing 8 widgets. 6 metrics up, 2 down."

Real-Time Update:
→ "Revenue updated to $1.25 million"
→ "3 metrics updated in the last minute"

Filter Applied:
→ "Date range changed to last 30 days. Refreshing data..."
→ "Data refreshed. Now showing 30-day view."

Widget Added:
→ "Conversion Rate widget added to position 5"

Alert Triggered:
→ "Alert: Revenue dropped below threshold. Current value: $92,000"

Error Occurred:
→ "Error: Failed to load User Growth widget. Retry available."
```

## 🌍 Internationalization (i18n)

### Translation Keys (Sample)
```json
{
  "dashboard.title": "Analytics Dashboard",
  "dashboard.customize": "Customize Dashboard",
  "dashboard.addWidget": "Add Widget",

  "widget.menu.refresh": "Refresh",
  "widget.menu.details": "View Details",
  "widget.menu.alert": "Create Alert",
  "widget.menu.export": "Export Data",
  "widget.menu.remove": "Remove",

  "error.connectionLost": "Connection lost. Attempting to reconnect...",
  "error.loadFailed": "Failed to load data",
  "error.saveFailed": "Failed to save layout changes",

  "metrics.revenue": "Total Revenue",
  "metrics.mrr": "Monthly Recurring Revenue",
  "metrics.conversionRate": "Conversion Rate",

  "help.shortcuts.title": "Keyboard Shortcuts",
  "help.shortcuts.filters": "Open filters panel",
  "help.shortcuts.customize": "Toggle edit mode",

  "alert.threshold.triggered": "Alert triggered: {metric} {condition} {threshold}",
  "notification.exported": "Report exported successfully",
  "notification.layoutSaved": "Layout saved"
}
```

### Number & Date Formatting
```typescript
// Locale-aware formatting
const formatCurrency = (value: number, locale: string) => {
  return new Intl.NumberFormat(locale, {
    style: 'currency',
    currency: getCurrencyForLocale(locale)
  }).format(value);
};

// en-US: $1,234,567.89
// de-DE: 1.234.567,89 €
// ja-JP: ¥1,234,568

const formatDate = (date: Date, locale: string) => {
  return new Intl.DateTimeFormat(locale, {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  }).format(date);
};

// en-US: Jan 10, 2025
// de-DE: 10. Jan. 2025
// ja-JP: 2025年1月10日
```

## 📖 Onboarding & First-Time Experience

### Welcome Flow
```
Step 1: Welcome Screen
Title: "Welcome to Analytics Dashboard"
Message: "Track your key metrics in real-time with customizable widgets and intelligent alerts."
Action: "Get Started"

Step 2: Choose Template
Title: "Choose a dashboard template"
Options:
- "Executive Overview" → High-level KPIs
- "Sales Dashboard" → Revenue and conversion metrics
- "Marketing Dashboard" → Campaign and engagement metrics
- "Start from Scratch" → Build your own

Step 3: Add First Widgets (Interactive)
Title: "Add your first widgets"
Message: "Select the metrics you want to track"
Preview: Shows how widgets will look
Action: "Add to Dashboard"

Step 4: Tutorial Tooltip
"💡 Tip: Click any widget to see detailed data"
"💡 Drag widgets to rearrange your dashboard"
"💡 Set up alerts to stay informed of important changes"

Completion:
Message: "Your dashboard is ready!"
Action: "Start Exploring" or "Take a Tour"
```

## 🔗 Related Documentation

- [Requirements](./requirements.md) - Content requirements
- [User Experience](./user-experience.md) - UX context for content
- [Testing Strategy](./testing-strategy.md) - Testing content strategies

---

[← Back to Dashboard Hub](./README.md) | [← Previous: Implementation](./implementation.md) | [Next: Testing Strategy →](./testing-strategy.md)

**Content Note**: This example demonstrates comprehensive content strategy for complex enterprise features with extensive user guidance, error handling, and accessibility requirements.

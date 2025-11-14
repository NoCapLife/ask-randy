---
title: Dashboard Feature - Implementation Guide
type: implementation
feature: example-dashboard
category: example
status: template-example
last_updated: 2025-01-10
developers: ["engineering-team"]
estimated_hours: 160
---

# Dashboard Feature - Implementation Guide

**Purpose**: Phased implementation plan for complex enterprise dashboard.
**Audience**: Development teams implementing the feature.
**File Size**: 🔴 Large (700 lines) - Comprehensive implementation for complex feature.

[← Back to Dashboard Hub](./README.md) | [← Previous: Technical Design](./technical-design.md) | [Next: Content Strategy →](./content-strategy.md)

---

## 📋 Implementation Phases

### Phase 1: Foundation (Week 1-2, 80 hours)
**Goal**: Set up core architecture, state management, and basic layout.

#### Checklist
- [ ] Project structure and TypeScript setup
- [ ] State management (Zustand/Redux) implementation
- [ ] API client and authentication
- [ ] Basic routing and navigation
- [ ] Grid layout system
- [ ] Widget registry and renderer
- [ ] Initial component library setup

### Phase 2: Core Widgets (Week 3-4, 80 hours)
**Goal**: Implement all standard widget types with data fetching.

#### Checklist
- [ ] Metric Card widget
- [ ] Line Chart widget (with Recharts/D3)
- [ ] Bar Chart widget
- [ ] Pie/Donut Chart widget
- [ ] Data Table widget with pagination
- [ ] Funnel Chart widget
- [ ] Widget skeleton loading states
- [ ] Error boundaries for widgets

### Phase 3: Real-Time Features (Week 5-6, 80 hours)
**Goal**: WebSocket integration and live data updates.

#### Checklist
- [ ] WebSocket client implementation
- [ ] Subscription management
- [ ] Real-time data synchronization
- [ ] Connection status indicator
- [ ] Reconnection logic with exponential backoff
- [ ] Fallback polling mechanism
- [ ] Update animations and transitions

### Phase 4: Customization (Week 7-8, 80 hours)
**Goal**: Dashboard customization and personalization features.

#### Checklist
- [ ] Drag-and-drop layout editing
- [ ] Widget library modal
- [ ] Add/remove widgets
- [ ] Resize widgets
- [ ] Layout persistence (backend integration)
- [ ] Save multiple dashboard configurations
- [ ] Share dashboards

### Phase 5: Filtering & Alerts (Week 9-10, 80 hours)
**Goal**: Advanced filtering and alert system.

#### Checklist
- [ ] Date range selector with presets
- [ ] Global filter panel
- [ ] Per-widget filters
- [ ] Filter persistence
- [ ] Alert creation UI
- [ ] Alert notification system
- [ ] Alert history and management

### Phase 6: Polish & Performance (Week 11-12, 80 hours)
**Goal**: Optimization, accessibility, and production readiness.

#### Checklist
- [ ] Performance optimization (virtualization, code splitting)
- [ ] Accessibility audit and fixes
- [ ] Mobile responsive layout
- [ ] Error handling and user feedback
- [ ] Analytics integration
- [ ] Documentation and help system
- [ ] Load testing and optimization

---

## 🔧 Detailed Implementation Steps

### Step 1: Set Up State Management

**File**: `store/dashboardSlice.ts`

```typescript
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface DashboardStore {
  // State
  layout: WidgetConfig[];
  isEditMode: boolean;
  dateRange: DateRange;
  filters: Filter[];
  connected: boolean;

  // Actions
  addWidget: (widget: WidgetConfig) => void;
  removeWidget: (id: string) => void;
  updateLayout: (layout: WidgetConfig[]) => void;
  toggleEditMode: () => void;
  setDateRange: (range: DateRange) => void;
  setFilters: (filters: Filter[]) => void;
  setConnected: (connected: boolean) => void;
}

export const useDashboardStore = create<DashboardStore>()(
  persist(
    (set) => ({
      // Initial state
      layout: [],
      isEditMode: false,
      dateRange: { start: '2025-01-01', end: '2025-01-10' },
      filters: [],
      connected: false,

      // Actions
      addWidget: (widget) =>
        set((state) => ({ layout: [...state.layout, widget] })),

      removeWidget: (id) =>
        set((state) => ({
          layout: state.layout.filter((w) => w.id !== id)
        })),

      updateLayout: (layout) => set({ layout }),

      toggleEditMode: () =>
        set((state) => ({ isEditMode: !state.isEditMode })),

      setDateRange: (dateRange) => set({ dateRange }),

      setFilters: (filters) => set({ filters }),

      setConnected: (connected) => set({ connected })
    }),
    {
      name: 'dashboard-storage', // localStorage key
      partialize: (state) => ({
        // Only persist these fields
        layout: state.layout,
        dateRange: state.dateRange,
        filters: state.filters
      })
    }
  )
);
```

### Step 2: Implement WebSocket Client

**File**: `services/websocketClient.ts`

```typescript
import { useDashboardStore } from '../store/dashboardSlice';

class WebSocketClient {
  private ws: WebSocket | null = null;
  private url: string;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 10;
  private subscriptions = new Set<string>();
  private reconnectTimeout: NodeJS.Timeout | null = null;

  constructor(url: string) {
    this.url = url;
  }

  connect(token: string): void {
    const wsUrl = `${this.url}?token=${token}`;
    this.ws = new WebSocket(wsUrl);

    this.ws.onopen = this.handleOpen.bind(this);
    this.ws.onmessage = this.handleMessage.bind(this);
    this.ws.onerror = this.handleError.bind(this);
    this.ws.onclose = this.handleClose.bind(this);
  }

  private handleOpen(): void {
    console.log('✅ WebSocket connected');
    useDashboardStore.getState().setConnected(true);
    this.reconnectAttempts = 0;

    // Re-subscribe to all metrics
    this.subscriptions.forEach((metricId) => {
      this.subscribe(metricId);
    });
  }

  private handleMessage(event: MessageEvent): void {
    try {
      const message: WebSocketMessage = JSON.parse(event.data);

      switch (message.type) {
        case 'metric_update':
          this.handleMetricUpdate(message.payload);
          break;
        case 'alert':
          this.handleAlert(message.payload);
          break;
        case 'error':
          console.error('WebSocket error:', message.payload);
          break;
      }
    } catch (error) {
      console.error('Failed to parse WebSocket message:', error);
    }
  }

  private handleMetricUpdate(payload: MetricUpdatePayload): void {
    // Update widget data in store
    const { widgetId, data } = payload;
    // Trigger store update (implementation depends on your store structure)
  }

  private handleAlert(payload: AlertPayload): void {
    // Show notification
    showNotification({
      title: 'Alert Triggered',
      message: payload.message,
      severity: payload.severity
    });
  }

  private handleError(error: Event): void {
    console.error('WebSocket error:', error);
  }

  private handleClose(): void {
    console.log('WebSocket closed');
    useDashboardStore.getState().setConnected(false);
    this.attemptReconnect();
  }

  subscribe(metricId: string): void {
    this.subscriptions.add(metricId);

    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.send({
        type: 'subscribe',
        metricId
      });
    }
  }

  unsubscribe(metricId: string): void {
    this.subscriptions.delete(metricId);

    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.send({
        type: 'unsubscribe',
        metricId
      });
    }
  }

  private send(message: any): void {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(message));
    }
  }

  private attemptReconnect(): void {
    if (this.reconnectAttempts >= this.maxReconnectAttempts) {
      console.error('Max reconnection attempts reached');
      return;
    }

    this.reconnectAttempts++;
    const delay = Math.min(1000 * Math.pow(2, this.reconnectAttempts), 30000);

    console.log(`Reconnecting in ${delay}ms... (attempt ${this.reconnectAttempts})`);

    this.reconnectTimeout = setTimeout(() => {
      this.connect(getAuthToken());
    }, delay);
  }

  disconnect(): void {
    if (this.reconnectTimeout) {
      clearTimeout(this.reconnectTimeout);
    }

    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }
}

export const wsClient = new WebSocketClient(
  process.env.NEXT_PUBLIC_WS_URL || 'ws://localhost:3001'
);
```

### Step 3: Create Metric Card Widget

**File**: `components/widgets/MetricCard.tsx`

```typescript
import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, TrendingDown } from 'lucide-react';
import { useWidgetData } from '../../hooks/useWidgetData';
import { Skeleton } from '../ui/Skeleton';

interface MetricCardProps {
  config: WidgetConfig;
}

export function MetricCard({ config }: MetricCardProps) {
  const { data, isLoading, error } = useWidgetData(config.id);

  if (isLoading) {
    return <MetricCardSkeleton />;
  }

  if (error) {
    return <MetricCardError error={error} />;
  }

  const { value, previousValue, label, unit } = data;
  const change = calculateChange(value, previousValue);
  const isPositive = change >= 0;

  return (
    <motion.div
      className="metric-card"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <div className="metric-card__header">
        <h3>{label}</h3>
        <MetricMenu config={config} />
      </div>

      <div className="metric-card__value">
        <AnimatedNumber
          value={value}
          unit={unit}
          className="metric-card__number"
        />
      </div>

      <div className="metric-card__trend">
        <TrendIndicator change={change} isPositive={isPositive} />
        <span className={`metric-card__change ${isPositive ? 'positive' : 'negative'}`}>
          {isPositive ? '+' : ''}{change.toFixed(2)}%
        </span>
        <span className="metric-card__comparison">
          vs previous period
        </span>
      </div>

      <Sparkline data={data.sparklineData} />
    </motion.div>
  );
}

function TrendIndicator({ change, isPositive }: { change: number; isPositive: boolean }) {
  const Icon = isPositive ? TrendingUp : TrendingDown;
  return (
    <Icon
      className={`trend-icon ${isPositive ? 'trend-up' : 'trend-down'}`}
      size={16}
    />
  );
}

function AnimatedNumber({ value, unit, className }: any) {
  return (
    <motion.span
      key={value}
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      className={className}
    >
      {formatNumber(value)}
      {unit && <span className="metric-card__unit">{unit}</span>}
    </motion.span>
  );
}

function calculateChange(current: number, previous: number): number {
  if (previous === 0) return 0;
  return ((current - previous) / previous) * 100;
}
```

### Step 4: Implement Drag-and-Drop Layout

**File**: `components/DashboardGrid.tsx`

```typescript
import React from 'react';
import { DndContext, DragEndEvent, useSensor, useSensors, PointerSensor } from '@dnd-kit/core';
import { SortableContext, arrayMove } from '@dnd-kit/sortable';
import { SortableWidget } from './SortableWidget';
import { useDashboardStore } from '../store/dashboardSlice';

export function DashboardGrid() {
  const { layout, isEditMode, updateLayout } = useDashboardStore();

  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: {
        distance: 8 // 8px drag threshold before starting
      }
    })
  );

  const handleDragEnd = (event: DragEndEvent) => {
    const { active, over } = event;

    if (over && active.id !== over.id) {
      const oldIndex = layout.findIndex((w) => w.id === active.id);
      const newIndex = layout.findIndex((w) => w.id === over.id);

      const newLayout = arrayMove(layout, oldIndex, newIndex);
      updateLayout(newLayout);

      // Persist to backend
      saveLayoutToBackend(newLayout);
    }
  };

  return (
    <DndContext sensors={sensors} onDragEnd={handleDragEnd}>
      <SortableContext items={layout.map((w) => w.id)}>
        <div
          className={`dashboard-grid ${isEditMode ? 'edit-mode' : ''}`}
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '16px'
          }}
        >
          {layout.map((widget) => (
            <SortableWidget key={widget.id} widget={widget} />
          ))}
        </div>
      </SortableContext>
    </DndContext>
  );
}

async function saveLayoutToBackend(layout: WidgetConfig[]): Promise<void> {
  try {
    await api.post('/dashboard/layout', { layout });
  } catch (error) {
    console.error('Failed to save layout:', error);
    showNotification({
      title: 'Error',
      message: 'Failed to save dashboard layout',
      severity: 'error'
    });
  }
}
```

### Step 5: Date Range Filter

**File**: `components/filters/DateRangeFilter.tsx`

```typescript
import React, { useState } from 'react';
import { Popover, PopoverTrigger, PopoverContent } from '../ui/Popover';
import { Calendar } from '../ui/Calendar';
import { useDashboardStore } from '../../store/dashboardSlice';

const QUICK_RANGES = [
  { label: 'Today', value: 'today' },
  { label: 'Yesterday', value: 'yesterday' },
  { label: 'Last 7 days', value: 'last-7-days' },
  { label: 'Last 30 days', value: 'last-30-days' },
  { label: 'This month', value: 'this-month' },
  { label: 'Last month', value: 'last-month' },
  { label: 'Custom', value: 'custom' }
];

export function DateRangeFilter() {
  const { dateRange, setDateRange } = useDashboardStore();
  const [selectedQuickRange, setSelectedQuickRange] = useState('last-7-days');
  const [showCustom, setShowCustom] = useState(false);

  const handleQuickRangeSelect = (value: string) => {
    setSelectedQuickRange(value);

    if (value === 'custom') {
      setShowCustom(true);
      return;
    }

    const range = calculateDateRange(value);
    setDateRange(range);
    setShowCustom(false);
  };

  const handleCustomRangeSelect = (range: DateRange) => {
    setDateRange(range);
    setShowCustom(false);
  };

  return (
    <Popover>
      <PopoverTrigger>
        <button className="date-range-trigger">
          {formatDateRange(dateRange)}
        </button>
      </PopoverTrigger>

      <PopoverContent>
        <div className="date-range-filter">
          <div className="quick-ranges">
            {QUICK_RANGES.map((range) => (
              <button
                key={range.value}
                className={`quick-range ${selectedQuickRange === range.value ? 'active' : ''}`}
                onClick={() => handleQuickRangeSelect(range.value)}
              >
                {range.label}
              </button>
            ))}
          </div>

          {showCustom && (
            <div className="custom-range">
              <Calendar
                mode="range"
                selected={dateRange}
                onSelect={handleCustomRangeSelect}
              />
            </div>
          )}
        </div>
      </PopoverContent>
    </Popover>
  );
}

function calculateDateRange(value: string): DateRange {
  const now = new Date();
  const ranges: Record<string, DateRange> = {
    'today': { start: startOfDay(now), end: endOfDay(now) },
    'yesterday': { start: startOfDay(subDays(now, 1)), end: endOfDay(subDays(now, 1)) },
    'last-7-days': { start: subDays(now, 7), end: now },
    'last-30-days': { start: subDays(now, 30), end: now },
    'this-month': { start: startOfMonth(now), end: endOfMonth(now) },
    'last-month': { start: startOfMonth(subMonths(now, 1)), end: endOfMonth(subMonths(now, 1)) }
  };

  return ranges[value] || ranges['last-7-days'];
}
```

## 🧪 Implementation Testing

### Test Each Phase
```typescript
// Phase 1: Foundation tests
describe('Dashboard Foundation', () => {
  test('loads initial layout from storage', () => {
    render(<Dashboard />);
    expect(screen.getByRole('main')).toBeInTheDocument();
  });

  test('state management works correctly', () => {
    const { result } = renderHook(() => useDashboardStore());
    act(() => result.current.addWidget(mockWidget));
    expect(result.current.layout).toHaveLength(1);
  });
});

// Phase 3: Real-time tests
describe('WebSocket Integration', () => {
  test('connects to WebSocket server', async () => {
    const mockWs = new MockWebSocket();
    wsClient.connect('test-token');
    await waitFor(() => {
      expect(mockWs.readyState).toBe(WebSocket.OPEN);
    });
  });

  test('handles metric updates', async () => {
    wsClient.subscribe('metric-1');
    mockWs.emit('metric_update', { widgetId: 'metric-1', data: { value: 100 } });
    await waitFor(() => {
      expect(screen.getByText('100')).toBeInTheDocument();
    });
  });
});
```

## 🔗 Related Documentation

- [Technical Design](./technical-design.md) - Architecture being implemented
- [Testing Strategy](./testing-strategy.md) - Testing each implementation phase
- [Content Strategy](./content-strategy.md) - UI copy for components

---

[← Back to Dashboard Hub](./README.md) | [← Previous: Technical Design](./technical-design.md) | [Next: Content Strategy →](./content-strategy.md)

**Implementation Note**: This is a large feature. Follow the phased approach and maintain test coverage at each phase.

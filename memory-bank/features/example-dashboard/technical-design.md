---
title: Dashboard Feature - Technical Design
type: technical-design
feature: example-dashboard
category: example
status: template-example
last_updated: 2025-01-10
architects: ["engineering-team", "platform-team"]
tech_stack: ["react", "typescript", "websockets", "redis", "postgresql"]
---

# Dashboard Feature - Technical Design

**Purpose**: Define architecture for complex enterprise dashboard with real-time data.
**Audience**: Senior engineers, architects, platform teams.
**File Size**: 🔴 Large (800 lines) - Comprehensive architecture for complex system.

[← Back to Dashboard Hub](./README.md) | [← Previous: User Experience](./user-experience.md) | [Next: Implementation →](./implementation.md)

---

## 🏗️ System Architecture

### High-Level Architecture
```
┌─────────────┐
│   Browser   │
│  (React)    │
└──────┬──────┘
       │ HTTPS/WSS
       ▼
┌─────────────────────┐
│  Load Balancer      │
│  (nginx/ALB)        │
└──────┬──────────────┘
       │
   ┌───┴───┐
   ▼       ▼
┌──────┐ ┌──────┐
│ API  │ │ API  │  ← Horizontal scaling
│Server│ │Server│
└───┬──┘ └───┬──┘
    │        │
    └────┬───┘
         │
    ┌────┴────────┬──────────┬──────────┐
    ▼             ▼          ▼          ▼
┌────────┐  ┌─────────┐ ┌────────┐ ┌──────────┐
│Postgres│  │  Redis  │ │WebSocket││ Analytics│
│   DB   │  │  Cache  │ │ Server  ││  Service │
└────────┘  └─────────┘ └────────┘ └──────────┘
```

### Component Architecture (Frontend)
```
src/
├── features/
│   └── dashboard/
│       ├── DashboardContainer.tsx       (Smart container)
│       ├── components/
│       │   ├── DashboardGrid.tsx       (Layout engine)
│       │   ├── widgets/
│       │   │   ├── MetricCard.tsx
│       │   │   ├── LineChart.tsx
│       │   │   ├── BarChart.tsx
│       │   │   ├── DataTable.tsx
│       │   │   └── index.ts
│       │   ├── filters/
│       │   │   ├── DateRangeFilter.tsx
│       │   │   ├── FilterPanel.tsx
│       │   │   └── SavedFilters.tsx
│       │   └── layout/
│       │       ├── EditMode.tsx
│       │       ├── WidgetLibrary.tsx
│       │       └── LayoutPresets.tsx
│       ├── hooks/
│       │   ├── useDashboardState.ts    (Main state management)
│       │   ├── useRealTimeData.ts      (WebSocket integration)
│       │   ├── useWidgetData.ts        (Data fetching per widget)
│       │   ├── useLayoutPersistence.ts (Save/load layouts)
│       │   └── useAlerts.ts            (Alert management)
│       ├── services/
│       │   ├── dashboardApi.ts         (API client)
│       │   ├── websocketClient.ts      (WebSocket manager)
│       │   ├── cacheManager.ts         (Client-side cache)
│       │   └── exportService.ts        (PDF/CSV export)
│       ├── store/
│       │   ├── dashboardSlice.ts       (Redux/Zustand slice)
│       │   ├── widgetSlice.ts
│       │   └── alertSlice.ts
│       ├── types/
│       │   ├── dashboard.types.ts
│       │   ├── widget.types.ts
│       │   └── api.types.ts
│       └── utils/
│           ├── chartFormatters.ts
│           ├── dateHelpers.ts
│           └── validators.ts
```

## 🔄 State Management Architecture

### Global State (Zustand/Redux)
```typescript
interface DashboardState {
  // Layout state
  layout: {
    widgets: WidgetConfig[];
    gridLayout: GridLayout;
    isEditMode: boolean;
  };

  // Data state
  data: {
    metrics: Record<string, MetricData>;
    timeSeries: Record<string, TimeSeriesData>;
    status: 'idle' | 'loading' | 'error';
    lastUpdated: Record<string, number>;
  };

  // Filter state
  filters: {
    dateRange: DateRange;
    segments: Segment[];
    customFilters: Filter[];
  };

  // User state
  user: {
    preferences: UserPreferences;
    savedDashboards: SavedDashboard[];
    alerts: Alert[];
  };

  // WebSocket state
  realTime: {
    connected: boolean;
    subscriptions: string[];
    updateQueue: Update[];
  };
}

// Actions
interface DashboardActions {
  // Layout actions
  addWidget: (widget: WidgetConfig) => void;
  removeWidget: (widgetId: string) => void;
  updateLayout: (layout: GridLayout) => void;
  toggleEditMode: () => void;

  // Data actions
  fetchMetrics: (widgetId: string) => Promise<void>;
  updateMetric: (widgetId: string, data: MetricData) => void;
  refreshAllWidgets: () => Promise<void>;

  // Filter actions
  setDateRange: (range: DateRange) => void;
  applyFilters: (filters: Filter[]) => void;
  saveFilterSet: (name: string) => Promise<void>;

  // Real-time actions
  connectWebSocket: () => void;
  disconnectWebSocket: () => void;
  subscribeToMetric: (metricId: string) => void;
}
```

### Local Component State
```typescript
// Individual widget manages its own UI state
function MetricCard({ config }: { config: WidgetConfig }) {
  // Local UI state
  const [isExpanded, setIsExpanded] = useState(false);
  const [showTooltip, setShowTooltip] = useState(false);

  // Global data from store
  const data = useWidgetData(config.id);
  const updateMetric = useDashboardStore(state => state.updateMetric);

  // ...
}
```

## 🌐 Real-Time Data Architecture

### WebSocket Integration
```typescript
class DashboardWebSocketClient {
  private ws: WebSocket | null = null;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 5;
  private subscriptions = new Set<string>();

  connect(url: string, token: string): void {
    this.ws = new WebSocket(`${url}?auth=${token}`);

    this.ws.onopen = () => {
      console.log('WebSocket connected');
      this.reconnectAttempts = 0;
      // Resubscribe to all metrics
      this.subscriptions.forEach(metricId => {
        this.subscribe(metricId);
      });
    };

    this.ws.onmessage = (event) => {
      const update: MetricUpdate = JSON.parse(event.data);
      this.handleUpdate(update);
    };

    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    this.ws.onclose = () => {
      console.log('WebSocket closed');
      this.attemptReconnect(url, token);
    };
  }

  subscribe(metricId: string): void {
    this.subscriptions.add(metricId);
    this.send({
      type: 'subscribe',
      metricId
    });
  }

  unsubscribe(metricId: string): void {
    this.subscriptions.delete(metricId);
    this.send({
      type: 'unsubscribe',
      metricId
    });
  }

  private handleUpdate(update: MetricUpdate): void {
    // Update store with new data
    useDashboardStore.getState().updateMetric(update.metricId, update.data);

    // Trigger animations
    this.notifyWidgetUpdate(update.metricId);
  }

  private attemptReconnect(url: string, token: string): void {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      const delay = Math.min(1000 * Math.pow(2, this.reconnectAttempts), 30000);
      setTimeout(() => this.connect(url, token), delay);
    }
  }
}
```

### Data Synchronization Strategy
```typescript
// Hybrid approach: Real-time + Polling fallback
class DataSyncManager {
  private realTimeEnabled = true;
  private pollingInterval: NodeJS.Timeout | null = null;

  initSync(widgetIds: string[]): void {
    // Primary: WebSocket for real-time
    if (this.realTimeEnabled) {
      widgetIds.forEach(id => wsClient.subscribe(id));

      // Fallback: Poll every 30s to catch missed updates
      this.pollingInterval = setInterval(() => {
        this.validateDataFreshness(widgetIds);
      }, 30000);
    } else {
      // Fallback: Polling only (every 5s)
      this.startPolling(widgetIds);
    }
  }

  private async validateDataFreshness(widgetIds: string[]): Promise<void> {
    const store = useDashboardStore.getState();
    const now = Date.now();

    widgetIds.forEach(async (id) => {
      const lastUpdated = store.data.lastUpdated[id] || 0;
      const staleness = now - lastUpdated;

      // If data is stale (>60s), refresh manually
      if (staleness > 60000) {
        await store.fetchMetrics(id);
      }
    });
  }

  private startPolling(widgetIds: string[]): void {
    this.pollingInterval = setInterval(async () => {
      const store = useDashboardStore.getState();
      await Promise.all(widgetIds.map(id => store.fetchMetrics(id)));
    }, 5000);
  }

  cleanup(): void {
    if (this.pollingInterval) {
      clearInterval(this.pollingInterval);
    }
    wsClient.disconnect();
  }
}
```

## 📊 Data Fetching & Caching

### React Query Integration
```typescript
// Widget data fetching with caching
export function useWidgetData(widgetId: string, config: WidgetConfig) {
  const { dateRange, filters } = useDashboardStore(state => state.filters);

  return useQuery({
    queryKey: ['widget', widgetId, dateRange, filters],
    queryFn: () => fetchWidgetData(widgetId, {
      dateRange,
      filters,
      ...config.queryParams
    }),
    staleTime: 30000, // Consider fresh for 30s
    cacheTime: 300000, // Keep in cache for 5min
    refetchInterval: config.realTime ? false : 60000, // Poll every 60s if not real-time
    refetchOnWindowFocus: true,
    retry: 3,
    retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000)
  });
}

// Prefetch related data
export function usePrefetchRelatedWidgets(widgetId: string) {
  const queryClient = useQueryClient();
  const relatedWidgets = getRelatedWidgets(widgetId);

  useEffect(() => {
    relatedWidgets.forEach(id => {
      queryClient.prefetchQuery({
        queryKey: ['widget', id],
        queryFn: () => fetchWidgetData(id)
      });
    });
  }, [widgetId, queryClient]);
}
```

### Multi-Level Caching
```typescript
class CacheManager {
  private memoryCache = new Map<string, CacheEntry>();
  private indexedDB: IDBDatabase | null = null;

  async get<T>(key: string): Promise<T | null> {
    // L1: Memory cache (fastest)
    const memCached = this.memoryCache.get(key);
    if (memCached && !this.isExpired(memCached)) {
      return memCached.data as T;
    }

    // L2: IndexedDB (persistent)
    const dbCached = await this.getFromIndexedDB<T>(key);
    if (dbCached && !this.isExpired(dbCached)) {
      // Promote to memory cache
      this.memoryCache.set(key, dbCached);
      return dbCached.data;
    }

    return null;
  }

  async set<T>(key: string, data: T, ttl: number): Promise<void> {
    const entry: CacheEntry = {
      data,
      timestamp: Date.now(),
      ttl
    };

    // Write to both caches
    this.memoryCache.set(key, entry);
    await this.setToIndexedDB(key, entry);
  }

  private isExpired(entry: CacheEntry): boolean {
    return Date.now() - entry.timestamp > entry.ttl;
  }
}
```

## 📈 Performance Optimizations

### Widget Virtualization
```typescript
// Only render visible widgets
export function DashboardGrid({ widgets }: { widgets: WidgetConfig[] }) {
  const gridRef = useRef<HTMLDivElement>(null);
  const visibleWidgets = useVirtualization(gridRef, widgets, {
    overscan: 2 // Render 2 extra widgets above/below viewport
  });

  return (
    <div ref={gridRef} className="dashboard-grid">
      {visibleWidgets.map(widget => (
        <WidgetRenderer key={widget.id} config={widget} />
      ))}
    </div>
  );
}
```

### Code Splitting
```typescript
// Lazy load widget types
const MetricCard = lazy(() => import('./widgets/MetricCard'));
const LineChart = lazy(() => import('./widgets/LineChart'));
const BarChart = lazy(() => import('./widgets/BarChart'));
const DataTable = lazy(() => import('./widgets/DataTable'));

const widgetComponents: Record<WidgetType, LazyExoticComponent<any>> = {
  'metric-card': MetricCard,
  'line-chart': LineChart,
  'bar-chart': BarChart,
  'data-table': DataTable
};

function WidgetRenderer({ config }: { config: WidgetConfig }) {
  const Component = widgetComponents[config.type];

  return (
    <Suspense fallback={<WidgetSkeleton />}>
      <Component config={config} />
    </Suspense>
  );
}
```

### Optimized Re-renders
```typescript
// Memoize expensive computations
const ChartData = memo(({ data, dateRange }: ChartDataProps) => {
  const processedData = useMemo(() => {
    return processTimeSeriesData(data, dateRange);
  }, [data, dateRange]);

  const chartOptions = useMemo(() => {
    return generateChartOptions(processedData);
  }, [processedData]);

  return <Chart data={processedData} options={chartOptions} />;
});

// Prevent unnecessary re-renders with React.memo + custom comparison
const Widget = memo(
  ({ config, data }: WidgetProps) => {
    return <WidgetContent config={config} data={data} />;
  },
  (prevProps, nextProps) => {
    // Custom comparison - only re-render if data actually changed
    return (
      prevProps.config.id === nextProps.config.id &&
      isEqual(prevProps.data, nextProps.data)
    );
  }
);
```

## 🔒 Security Architecture

### Authentication & Authorization
```typescript
// RBAC middleware
interface Permission {
  resource: string;
  action: 'read' | 'write' | 'delete';
}

class PermissionManager {
  private userPermissions: Permission[] = [];

  async loadUserPermissions(): Promise<void> {
    const response = await api.get('/user/permissions');
    this.userPermissions = response.data;
  }

  canAccess(widgetConfig: WidgetConfig): boolean {
    const requiredPermission = {
      resource: widgetConfig.dataSource,
      action: 'read' as const
    };

    return this.userPermissions.some(p =>
      p.resource === requiredPermission.resource &&
      p.action === requiredPermission.action
    );
  }
}

// Widget-level permission check
function SecureWidget({ config }: { config: WidgetConfig }) {
  const permissions = usePermissions();

  if (!permissions.canAccess(config)) {
    return <NoPermissionMessage />;
  }

  return <WidgetRenderer config={config} />;
}
```

### Data Encryption
```typescript
// Sensitive data encryption in transit and at rest
class SecureDataService {
  async fetchSensitiveMetric(metricId: string): Promise<MetricData> {
    const encryptedResponse = await api.get(`/metrics/${metricId}`, {
      headers: {
        'X-Encryption': 'AES-256-GCM'
      }
    });

    // Decrypt client-side using session key
    return this.decrypt(encryptedResponse.data);
  }

  private decrypt(encryptedData: string): MetricData {
    // Client-side decryption implementation
    // Uses session key from secure auth flow
  }
}
```

## 🔗 Related Documentation

- [Requirements](./requirements.md) - Requirements driving architecture
- [Implementation](./implementation.md) - How to implement this architecture
- [Testing Strategy](./testing-strategy.md) - Testing the architecture
- [Decisions](./decisions.md) - Key architectural decisions

---

[← Back to Dashboard Hub](./README.md) | [← Previous: User Experience](./user-experience.md) | [Next: Implementation →](./implementation.md)

**Architecture Note**: This example demonstrates patterns for building scalable, real-time, enterprise dashboards with proper state management, caching, security, and performance optimization.

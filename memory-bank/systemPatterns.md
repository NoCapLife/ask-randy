---
owner: [Project Owner]
last_updated: 2025-01-10
size: 🟡
status: template
sources_of_truth: [systemPatterns.md]
related_files: [techContext.md, projectbrief.md, AI_GUIDE.md]
---

# System Patterns: Architecture & Design

**Purpose:** Core architecture principles, design patterns, and component relationships
**Status:** Template - customize for your project's specific architecture
**Last Updated:** [Date]

## Core Architecture Principles

### Modular Design
- **Component Isolation**: Self-contained modules with clear boundaries
- **Configuration Layer**: Centralized settings and parameters
- **Integration Layer**: Standardized connectors for external systems
- **Monitoring Layer**: Observability, logging, and health checks

### Data Flow Pattern
```
Input Sources → Processing Engine → Business Logic → Data Storage → Output Channels
```

**Key Characteristics:**
- Unidirectional data flow for predictability
- Clear separation of concerns
- Testable at each layer
- Observable state transitions

## Key Design Patterns

### 1. Component Architecture
- **Core Engine**: Base application framework
- **Module System**: Feature-based organization
- **Configuration**: Environment-based settings
- **Discovery**: Automatic component loading

**Example Structure:**
```
src/
├── core/                  # Core framework
├── modules/              # Feature modules
├── config/               # Configuration
└── shared/               # Shared utilities
```

### 2. Event-Driven Design
- **Triggers**: Time-based, user-based, or system-based events
- **Handlers**: Automated responses to specific events
- **Queuing**: Background processing for non-urgent tasks
- **Notification**: Status updates and completion alerts

**Event Flow:**
```
Event Source → Event Bus → Event Handler → Action Execution → Event Log
```

### 3. State Management
- **Context Gathering**: Collect relevant application state
- **State Updates**: Controlled state modifications
- **State Persistence**: Durable storage of important state
- **State Recovery**: Restoration after failures

## Component Relationships

### Core Components
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Application   │────│  Business Logic │────│  Data Layer     │
│   Interface     │    │   Engine        │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Configuration  │────│    Logging      │────│   Monitoring    │
│   Management    │    │   & Metrics     │    │  & Alerting     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Integration Points
- **User Interface**: Web, mobile, or CLI interactions
- **APIs**: External service integration
- **Database**: Persistent data storage
- **File System**: File-based operations
- **Third-Party Services**: External dependencies

## Feature Organization Patterns

### 1. Feature-Based Structure
```
features/
├── authentication/
│   ├── components/       # UI components
│   ├── hooks/           # Custom hooks
│   ├── services/        # Business logic
│   └── types/           # TypeScript types
├── dashboard/
│   ├── components/
│   ├── hooks/
│   └── services/
└── settings/
    ├── components/
    └── services/
```

**Benefits:**
- Easy to locate related code
- Clear feature boundaries
- Simplified testing and maintenance
- Natural scaling as features grow

### 2. Layer-Based Structure
```
src/
├── presentation/        # UI layer
│   ├── pages/
│   └── components/
├── application/        # Business logic
│   ├── services/
│   └── use-cases/
├── domain/             # Core domain models
│   ├── entities/
│   └── value-objects/
└── infrastructure/     # Technical details
    ├── api/
    └── database/
```

**Benefits:**
- Clear separation of concerns
- Enforces dependency rules
- Promotes reusability
- Supports clean architecture

### 3. Hybrid Approach
Combine feature-based and layer-based organization:
```
features/
├── authentication/
│   ├── presentation/   # UI components
│   ├── application/    # Business logic
│   └── infrastructure/ # API/DB access
└── dashboard/
    ├── presentation/
    ├── application/
    └── infrastructure/
```

## Common Application Patterns

### 1. Request/Response Pattern
**Use Case:** Synchronous operations requiring immediate feedback

```typescript
// Request handling pattern
async function handleRequest(request: Request): Promise<Response> {
  // 1. Validate input
  const validated = validateRequest(request);

  // 2. Execute business logic
  const result = await executeBusinessLogic(validated);

  // 3. Format response
  return formatResponse(result);
}
```

### 2. Command Pattern
**Use Case:** Encapsulating actions as objects for flexibility

```typescript
// Command interface
interface Command {
  execute(): Promise<void>;
  undo(): Promise<void>;
}

// Command implementation
class CreateUserCommand implements Command {
  async execute() { /* create user */ }
  async undo() { /* delete user */ }
}
```

### 3. Observer Pattern
**Use Case:** Notifying multiple components of state changes

```typescript
// Observable state management
class StateManager {
  private observers: Observer[] = [];

  subscribe(observer: Observer) {
    this.observers.push(observer);
  }

  notify(event: Event) {
    this.observers.forEach(obs => obs.update(event));
  }
}
```

### 4. Repository Pattern
**Use Case:** Abstracting data access logic

```typescript
// Repository interface
interface UserRepository {
  findById(id: string): Promise<User | null>;
  save(user: User): Promise<void>;
  delete(id: string): Promise<void>;
}

// Implementation can swap between databases
class SupabaseUserRepository implements UserRepository {
  // Supabase-specific implementation
}
```

## Error Handling & Resilience

### Failure Recovery Strategies

#### 1. Retry Logic
```typescript
async function withRetry<T>(
  operation: () => Promise<T>,
  maxRetries: number = 3
): Promise<T> {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === maxRetries) throw error;
      await delay(Math.pow(2, attempt) * 1000); // Exponential backoff
    }
  }
  throw new Error('Retry exhausted');
}
```

#### 2. Fallback Mechanisms
```typescript
async function withFallback<T>(
  primary: () => Promise<T>,
  fallback: () => Promise<T>
): Promise<T> {
  try {
    return await primary();
  } catch (error) {
    console.warn('Primary operation failed, using fallback');
    return await fallback();
  }
}
```

#### 3. Circuit Breaker
```typescript
class CircuitBreaker {
  private failures = 0;
  private state: 'CLOSED' | 'OPEN' | 'HALF_OPEN' = 'CLOSED';

  async execute<T>(operation: () => Promise<T>): Promise<T> {
    if (this.state === 'OPEN') {
      throw new Error('Circuit breaker is OPEN');
    }

    try {
      const result = await operation();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }

  private onSuccess() {
    this.failures = 0;
    this.state = 'CLOSED';
  }

  private onFailure() {
    this.failures++;
    if (this.failures >= 3) {
      this.state = 'OPEN';
    }
  }
}
```

### Monitoring & Observability

#### Health Checks
```typescript
interface HealthCheck {
  name: string;
  status: 'healthy' | 'degraded' | 'unhealthy';
  lastCheck: Date;
  message?: string;
}

async function performHealthChecks(): Promise<HealthCheck[]> {
  return Promise.all([
    checkDatabase(),
    checkExternalAPI(),
    checkFileSystem(),
    checkMemoryUsage(),
  ]);
}
```

#### Structured Logging
```typescript
// Log levels and context
logger.info('User action', {
  userId: user.id,
  action: 'login',
  timestamp: new Date(),
  metadata: { /* additional context */ }
});

logger.error('Operation failed', {
  error: error.message,
  stack: error.stack,
  context: { /* failure context */ }
});
```

#### Performance Metrics
```typescript
// Track key metrics
interface Metrics {
  requestDuration: number;
  requestCount: number;
  errorRate: number;
  activeUsers: number;
}

// Metric collection
function trackMetric(name: string, value: number) {
  metrics.record(name, value, {
    timestamp: Date.now(),
    tags: { /* categorization */ }
  });
}
```

## Security & Privacy Patterns

### Authentication & Authorization

#### Authentication Flow
```
User Login → Credentials Validation → Token Generation → Session Storage → Protected Routes
```

#### Authorization Pattern
```typescript
// Role-based access control
interface Permission {
  resource: string;
  action: 'read' | 'write' | 'delete';
}

function checkPermission(user: User, permission: Permission): boolean {
  return user.roles.some(role =>
    role.permissions.includes(permission)
  );
}

// Middleware for route protection
function requirePermission(permission: Permission) {
  return (req, res, next) => {
    if (!checkPermission(req.user, permission)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    next();
  };
}
```

### Data Protection

#### Encryption Patterns
```typescript
// Encrypt sensitive data before storage
async function encryptData(data: string): Promise<string> {
  // Use environment-specific encryption key
  const key = process.env.ENCRYPTION_KEY;
  return encrypt(data, key);
}

// Decrypt when needed
async function decryptData(encrypted: string): Promise<string> {
  const key = process.env.ENCRYPTION_KEY;
  return decrypt(encrypted, key);
}
```

#### Input Validation
```typescript
// Validate all external input
function validateUserInput(input: unknown): ValidatedInput {
  // Use schema validation (Zod, Yup, etc.)
  const schema = z.object({
    email: z.string().email(),
    name: z.string().min(1).max(100),
    age: z.number().int().positive(),
  });

  return schema.parse(input);
}
```

## Scalability Considerations

### Performance Optimization

#### Caching Strategy
```typescript
// Multi-layer caching
class CacheManager {
  private memoryCache = new Map();
  private redisCache = new RedisClient();

  async get(key: string): Promise<any> {
    // Check memory cache first (fastest)
    if (this.memoryCache.has(key)) {
      return this.memoryCache.get(key);
    }

    // Check Redis cache (fast)
    const redisValue = await this.redisCache.get(key);
    if (redisValue) {
      this.memoryCache.set(key, redisValue);
      return redisValue;
    }

    // Fetch from database (slow)
    const dbValue = await database.query(key);
    await this.set(key, dbValue);
    return dbValue;
  }

  async set(key: string, value: any, ttl: number = 3600) {
    this.memoryCache.set(key, value);
    await this.redisCache.set(key, value, ttl);
  }
}
```

#### Batch Processing
```typescript
// Process items in batches for efficiency
async function processBatch<T>(
  items: T[],
  processor: (item: T) => Promise<void>,
  batchSize: number = 50
) {
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    await Promise.all(batch.map(processor));
  }
}
```

#### Lazy Loading
```typescript
// Load data only when needed
class LazyResource {
  private data: any = null;

  async getData() {
    if (!this.data) {
      this.data = await this.loadData();
    }
    return this.data;
  }

  private async loadData() {
    // Expensive operation
    return fetchFromDatabase();
  }
}
```

### Growth Accommodation

#### Horizontal Scaling
- **Stateless Services**: Design services to be stateless for easy replication
- **Load Balancing**: Distribute traffic across multiple instances
- **Database Sharding**: Partition data across multiple databases
- **Microservices**: Break monolith into independently scalable services

#### Vertical Scaling
- **Resource Optimization**: Efficient memory and CPU usage
- **Database Indexing**: Optimize query performance
- **Connection Pooling**: Reuse database connections
- **Async Processing**: Non-blocking operations

## Testing Patterns

### Unit Testing
```typescript
// Test individual components in isolation
describe('UserService', () => {
  it('should create a new user', async () => {
    const mockRepository = createMockRepository();
    const service = new UserService(mockRepository);

    const user = await service.createUser({
      email: 'test@example.com',
      name: 'Test User'
    });

    expect(user.email).toBe('test@example.com');
    expect(mockRepository.save).toHaveBeenCalledOnce();
  });
});
```

### Integration Testing
```typescript
// Test component interactions
describe('Authentication Flow', () => {
  it('should authenticate user and create session', async () => {
    const app = createTestApp();

    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'password' });

    expect(response.status).toBe(200);
    expect(response.body.token).toBeDefined();
  });
});
```

### End-to-End Testing
```typescript
// Test complete user workflows
test('User can complete checkout process', async ({ page }) => {
  await page.goto('/products');
  await page.click('[data-testid="add-to-cart"]');
  await page.goto('/cart');
  await page.click('[data-testid="checkout"]');
  await page.fill('[name="email"]', 'test@example.com');
  await page.click('[data-testid="submit-order"]');

  await expect(page.locator('.success-message')).toBeVisible();
});
```

## Documentation Patterns

### Code Documentation
```typescript
/**
 * Processes user payment and creates order
 *
 * @param userId - Unique identifier for the user
 * @param items - Array of items to purchase
 * @param paymentMethod - Payment method to use
 * @returns Order confirmation with order ID
 * @throws {PaymentError} If payment processing fails
 * @throws {ValidationError} If items are invalid
 *
 * @example
 * const order = await processOrder('user123', items, 'credit_card');
 * console.log(order.id); // 'order_abc123'
 */
async function processOrder(
  userId: string,
  items: CartItem[],
  paymentMethod: PaymentMethod
): Promise<OrderConfirmation> {
  // Implementation
}
```

### Architecture Decision Records (ADR)
Keep decisions documented in `memory-bank/features/[feature]/decisions.md`:
- **Context**: What situation led to this decision?
- **Decision**: What did we decide to do?
- **Consequences**: What are the trade-offs?
- **Alternatives**: What other options were considered?

## Related Documentation

- **Technical Context**: `techContext.md` - Technology stack and development setup
- **Project Brief**: `projectbrief.md` - Project goals and scope
- **AI Guide**: `AI_GUIDE.md` - Efficient AI assistant usage patterns
- **Feature Docs**: `features/[name]/technical-design.md` - Feature-specific patterns

---

**Navigation:** [Back to startHere.md](./startHere.md) | [Tech Context](./techContext.md) | [Project Brief](./projectbrief.md)

---
owner: [Project Owner]
last_updated: 2025-01-10
size: 🟡
status: template
sources_of_truth: [techContext.md]
related_files: [systemPatterns.md, projectbrief.md, progress.md]
---

# Technical Context: Technology Stack & Development Setup

**Purpose:** Technical foundation, development environment, and implementation constraints
**Status:** Template - customize for your project's technology choices
**Last Updated:** [Date]

## Technology Stack

### Core Technologies
- **Primary Language**: [e.g., TypeScript, Python, Go, Rust]
- **Framework**: [e.g., Next.js, React, Django, Express]
- **Database**: [e.g., PostgreSQL, MongoDB, MySQL]
- **Authentication**: [e.g., Firebase Auth, Auth0, Supabase Auth]
- **State Management**: [e.g., React Query, Redux, Zustand]
- **Styling**: [e.g., Tailwind CSS, styled-components, CSS Modules]

### Development Environment
- **OS**: [e.g., macOS, Linux, Windows]
- **Runtime**: [e.g., Node.js 20+, Python 3.11+, Go 1.21+]
- **Package Manager**: [e.g., npm, pnpm, yarn, pip, poetry]
- **Code Editor**: [e.g., VS Code, Cursor, Vim]
- **Version Control**: Git
- **CI/CD**: [e.g., GitHub Actions, GitLab CI, CircleCI]

### Key Libraries & Frameworks

#### Frontend (Example: React/Next.js Stack)
```json
{
  "core": {
    "react": "^18.2.0",
    "next": "^14.0.0",
    "typescript": "^5.0.0"
  },
  "state_management": {
    "@tanstack/react-query": "^5.0.0",
    "zustand": "^4.4.0"
  },
  "ui_components": {
    "@radix-ui/react-*": "^1.0.0",
    "tailwindcss": "^3.3.0",
    "class-variance-authority": "^0.7.0"
  },
  "forms_validation": {
    "react-hook-form": "^7.48.0",
    "zod": "^3.22.0"
  },
  "utilities": {
    "date-fns": "^2.30.0",
    "lodash": "^4.17.21"
  }
}
```

#### Backend (Example: Node.js/API Stack)
```json
{
  "server": {
    "express": "^4.18.0",
    "fastify": "^4.24.0"
  },
  "database": {
    "@supabase/supabase-js": "^2.38.0",
    "prisma": "^5.6.0",
    "drizzle-orm": "^0.29.0"
  },
  "authentication": {
    "jsonwebtoken": "^9.0.0",
    "bcrypt": "^5.1.0"
  },
  "validation": {
    "zod": "^3.22.0",
    "joi": "^17.11.0"
  },
  "utilities": {
    "winston": "^3.11.0",
    "dotenv": "^16.3.0"
  }
}
```

#### Testing
```json
{
  "unit_testing": {
    "vitest": "^1.0.0",
    "@testing-library/react": "^14.1.0"
  },
  "e2e_testing": {
    "@playwright/test": "^1.40.0"
  },
  "mocking": {
    "msw": "^2.0.0"
  }
}
```

## Development Setup

### Directory Structure
```
project-root/
├── app/                    # Next.js app directory (routes)
│   ├── (auth)/            # Auth route group
│   ├── (dashboard)/       # Dashboard route group
│   ├── api/               # API routes
│   └── layout.tsx         # Root layout
├── components/            # React components
│   ├── ui/               # Reusable UI components
│   ├── features/         # Feature-specific components
│   └── layouts/          # Layout components
├── lib/                   # Utility libraries
│   ├── hooks/            # Custom React hooks
│   ├── utils/            # Utility functions
│   ├── types/            # TypeScript type definitions
│   └── constants/        # Constants and configuration
├── public/                # Static assets
├── memory-bank/          # Project documentation
├── tests/                # Test files
│   ├── unit/             # Unit tests
│   ├── integration/      # Integration tests
│   └── e2e/              # End-to-end tests
├── scripts/              # Build and utility scripts
└── config/               # Configuration files
```

### Alternative Structure (Backend-focused)
```
project-root/
├── src/
│   ├── api/              # API routes/controllers
│   ├── services/         # Business logic
│   ├── repositories/     # Data access layer
│   ├── models/           # Data models
│   ├── middleware/       # Express/Fastify middleware
│   ├── utils/            # Utility functions
│   └── types/            # TypeScript types
├── tests/                # Test files
├── migrations/           # Database migrations
├── scripts/              # Utility scripts
└── config/               # Configuration files
```

### Environment Configuration

#### Development Environment
```bash
# .env.local or .env.development
NODE_ENV=development
PORT=3000

# Database
DATABASE_URL=postgresql://localhost:5432/myapp_dev
REDIS_URL=redis://localhost:6379

# Authentication
JWT_SECRET=your_development_jwt_secret
SESSION_SECRET=your_development_session_secret

# External APIs (use test/sandbox keys)
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
OPENAI_API_KEY=sk-test-...

# Feature Flags
ENABLE_ANALYTICS=false
ENABLE_DEBUG_MODE=true
```

#### Production Environment
```bash
# .env.production (NEVER commit real values)
NODE_ENV=production
PORT=443

# Database (use environment variables in hosting platform)
DATABASE_URL=${DATABASE_URL}
REDIS_URL=${REDIS_URL}

# Authentication (use secrets manager)
JWT_SECRET=${JWT_SECRET}
SESSION_SECRET=${SESSION_SECRET}

# External APIs (use production keys)
STRIPE_PUBLIC_KEY=${STRIPE_PUBLIC_KEY}
STRIPE_SECRET_KEY=${STRIPE_SECRET_KEY}

# Feature Flags
ENABLE_ANALYTICS=true
ENABLE_DEBUG_MODE=false
```

#### Environment Variable Validation
```typescript
// lib/env.ts - Validate environment variables at startup
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  STRIPE_SECRET_KEY: z.string().startsWith('sk_'),
});

// Validate on app startup
export const env = envSchema.parse(process.env);
```

### Installation & Setup

#### Initial Setup
```bash
# Clone repository
git clone https://github.com/your-org/your-project.git
cd your-project

# Install dependencies
npm install

# Copy environment template
cp .env.example .env.local

# Setup database
npm run db:setup
npm run db:migrate

# Generate types (if using Prisma/Drizzle)
npm run db:generate

# Run development server
npm run dev
```

#### Database Setup
```bash
# Using Supabase
supabase start                    # Start local Supabase
supabase db reset                 # Reset and migrate database
supabase gen types typescript     # Generate TypeScript types

# Using Prisma
npx prisma migrate dev            # Run migrations
npx prisma generate               # Generate Prisma client
npx prisma studio                 # Open database GUI

# Using raw SQL
psql -h localhost -U postgres -d myapp < schema.sql
```

#### SSL/HTTPS Setup (for local development)
```bash
# Using mkcert for local HTTPS
brew install mkcert              # macOS
mkcert -install                  # Install CA
mkcert localhost 127.0.0.1       # Generate certificate

# Configure Next.js for HTTPS
npm run dev:https                # Custom script
```

## API Integrations

### External Services

#### Authentication Providers
```typescript
// Firebase Auth configuration
import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
};

export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
```

#### Database Client
```typescript
// Supabase client configuration
import { createClient } from '@supabase/supabase-js';

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
  {
    auth: {
      persistSession: true,
      autoRefreshToken: true,
    },
  }
);
```

#### Third-Party APIs
```typescript
// API client with retry logic
import { z } from 'zod';

class APIClient {
  constructor(private baseUrl: string, private apiKey: string) {}

  async request<T>(
    endpoint: string,
    options?: RequestInit,
    retries = 3
  ): Promise<T> {
    for (let i = 0; i < retries; i++) {
      try {
        const response = await fetch(`${this.baseUrl}${endpoint}`, {
          ...options,
          headers: {
            'Authorization': `Bearer ${this.apiKey}`,
            'Content-Type': 'application/json',
            ...options?.headers,
          },
        });

        if (!response.ok) {
          throw new Error(`API error: ${response.status}`);
        }

        return await response.json();
      } catch (error) {
        if (i === retries - 1) throw error;
        await this.delay(Math.pow(2, i) * 1000);
      }
    }
    throw new Error('Max retries exceeded');
  }

  private delay(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

### Rate Limiting & Error Handling

#### Client-Side Rate Limiting
```typescript
// Rate limiter for API calls
class RateLimiter {
  private requests: number[] = [];

  constructor(
    private maxRequests: number,
    private windowMs: number
  ) {}

  async acquire(): Promise<void> {
    const now = Date.now();
    this.requests = this.requests.filter(time => time > now - this.windowMs);

    if (this.requests.length >= this.maxRequests) {
      const oldestRequest = this.requests[0];
      const waitTime = oldestRequest + this.windowMs - now;
      await new Promise(resolve => setTimeout(resolve, waitTime));
      return this.acquire();
    }

    this.requests.push(now);
  }
}

// Usage
const limiter = new RateLimiter(10, 60000); // 10 requests per minute
await limiter.acquire();
await apiCall();
```

## Data Management

### Local Storage Strategy

#### Browser Storage
```typescript
// Type-safe local storage wrapper
class TypedStorage<T> {
  constructor(private key: string, private schema: z.ZodSchema<T>) {}

  get(): T | null {
    try {
      const value = localStorage.getItem(this.key);
      if (!value) return null;
      return this.schema.parse(JSON.parse(value));
    } catch {
      return null;
    }
  }

  set(value: T): void {
    localStorage.setItem(this.key, JSON.stringify(value));
  }

  remove(): void {
    localStorage.removeItem(this.key);
  }
}

// Usage
const userPreferences = new TypedStorage('user-prefs', userPrefsSchema);
```

#### Database Caching
```typescript
// Redis caching layer
import Redis from 'ioredis';

class CacheService {
  private redis = new Redis(process.env.REDIS_URL);

  async get<T>(key: string): Promise<T | null> {
    const value = await this.redis.get(key);
    return value ? JSON.parse(value) : null;
  }

  async set(key: string, value: any, ttl: number = 3600): Promise<void> {
    await this.redis.setex(key, ttl, JSON.stringify(value));
  }

  async invalidate(pattern: string): Promise<void> {
    const keys = await this.redis.keys(pattern);
    if (keys.length > 0) {
      await this.redis.del(...keys);
    }
  }
}
```

### Data Privacy & Security

#### Encryption at Rest
```typescript
// Encrypt sensitive data before storage
import crypto from 'crypto';

class EncryptionService {
  private algorithm = 'aes-256-gcm';
  private key = Buffer.from(process.env.ENCRYPTION_KEY!, 'hex');

  encrypt(text: string): { encrypted: string; iv: string; tag: string } {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(this.algorithm, this.key, iv);

    let encrypted = cipher.update(text, 'utf8', 'hex');
    encrypted += cipher.final('hex');

    return {
      encrypted,
      iv: iv.toString('hex'),
      tag: cipher.getAuthTag().toString('hex'),
    };
  }

  decrypt(encrypted: string, iv: string, tag: string): string {
    const decipher = crypto.createDecipheriv(
      this.algorithm,
      this.key,
      Buffer.from(iv, 'hex')
    );
    decipher.setAuthTag(Buffer.from(tag, 'hex'));

    let decrypted = decipher.update(encrypted, 'hex', 'utf8');
    decrypted += decipher.final('utf8');

    return decrypted;
  }
}
```

## Monitoring & Observability

### Logging Strategy

#### Structured Logging
```typescript
// Winston logger configuration
import winston from 'winston';

export const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: {
    service: 'your-app-name',
    environment: process.env.NODE_ENV,
  },
  transports: [
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' }),
    ...(process.env.NODE_ENV === 'development'
      ? [new winston.transports.Console({ format: winston.format.simple() })]
      : []),
  ],
});

// Usage
logger.info('User action', {
  userId: user.id,
  action: 'login',
  metadata: { ip: req.ip },
});
```

### Performance Monitoring

#### Application Metrics
```typescript
// Simple metrics collection
class MetricsCollector {
  private metrics = new Map<string, number[]>();

  record(name: string, value: number): void {
    if (!this.metrics.has(name)) {
      this.metrics.set(name, []);
    }
    this.metrics.get(name)!.push(value);
  }

  getAverage(name: string): number {
    const values = this.metrics.get(name) || [];
    return values.reduce((a, b) => a + b, 0) / values.length || 0;
  }

  getPercentile(name: string, percentile: number): number {
    const values = (this.metrics.get(name) || []).sort((a, b) => a - b);
    const index = Math.ceil((percentile / 100) * values.length) - 1;
    return values[index] || 0;
  }
}

// Usage
const metrics = new MetricsCollector();
metrics.record('api.response_time', 145);
console.log(metrics.getPercentile('api.response_time', 95)); // p95
```

#### Request Tracking
```typescript
// Middleware for request duration tracking
export function trackRequestDuration(req: Request, res: Response, next: NextFunction) {
  const start = Date.now();

  res.on('finish', () => {
    const duration = Date.now() - start;
    logger.info('Request completed', {
      method: req.method,
      path: req.path,
      statusCode: res.statusCode,
      duration,
    });
    metrics.record('request.duration', duration);
  });

  next();
}
```

## Security Considerations

### Authentication & Authorization

#### JWT Token Management
```typescript
import jwt from 'jsonwebtoken';

interface TokenPayload {
  userId: string;
  email: string;
  roles: string[];
}

export function generateToken(payload: TokenPayload): string {
  return jwt.sign(payload, process.env.JWT_SECRET!, {
    expiresIn: '7d',
    issuer: 'your-app-name',
  });
}

export function verifyToken(token: string): TokenPayload {
  return jwt.verify(token, process.env.JWT_SECRET!) as TokenPayload;
}

// Middleware
export function requireAuth(req: Request, res: Response, next: NextFunction) {
  const token = req.headers.authorization?.replace('Bearer ', '');

  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }

  try {
    req.user = verifyToken(token);
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}
```

### Input Validation & Sanitization

#### Request Validation
```typescript
import { z } from 'zod';

// Schema definition
const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  password: z.string().min(8).max(100),
  age: z.number().int().min(18).optional(),
});

// Validation middleware
export function validateRequest(schema: z.ZodSchema) {
  return (req: Request, res: Response, next: NextFunction) => {
    try {
      req.body = schema.parse(req.body);
      next();
    } catch (error) {
      if (error instanceof z.ZodError) {
        return res.status(400).json({
          error: 'Validation failed',
          details: error.errors,
        });
      }
      next(error);
    }
  };
}

// Usage in route
app.post('/api/users', validateRequest(createUserSchema), createUserHandler);
```

### CORS & Security Headers

#### Security Configuration
```typescript
// Express security middleware
import helmet from 'helmet';
import cors from 'cors';

app.use(helmet()); // Set security headers
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:3000'],
  credentials: true,
}));

// Rate limiting
import rateLimit from 'express-rate-limit';

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests, please try again later',
});

app.use('/api/', limiter);
```

## Development Constraints

### Performance Requirements
- **Response Time**: < 200ms for API endpoints (p95)
- **Page Load**: < 2s for initial page load
- **Time to Interactive**: < 3s for interactive state
- **Bundle Size**: < 200KB for initial JavaScript bundle

### Reliability Requirements
- **Uptime**: 99.9% availability target
- **Error Rate**: < 0.1% of requests
- **Data Integrity**: Zero data loss tolerance
- **Backup Frequency**: Daily automated backups

### Scalability Targets
- **Concurrent Users**: Support for [X] concurrent users
- **Requests per Second**: Handle [X] req/s
- **Database Size**: Efficient queries up to [X] GB
- **Storage**: Accommodate [X] TB of user data

## Testing Strategy

### Unit Testing
```typescript
// Component test example (Vitest + Testing Library)
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';

describe('Button', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('calls onClick when clicked', async () => {
    const onClick = vi.fn();
    render(<Button onClick={onClick}>Click me</Button>);

    await userEvent.click(screen.getByText('Click me'));
    expect(onClick).toHaveBeenCalledOnce();
  });
});
```

### Integration Testing
```typescript
// API integration test
import { describe, it, expect, beforeAll } from 'vitest';
import request from 'supertest';
import { app } from '../app';

describe('User API', () => {
  beforeAll(async () => {
    await setupTestDatabase();
  });

  it('should create a new user', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({
        email: 'test@example.com',
        name: 'Test User',
        password: 'password123',
      });

    expect(response.status).toBe(201);
    expect(response.body.email).toBe('test@example.com');
  });
});
```

### E2E Testing
```typescript
// Playwright test
import { test, expect } from '@playwright/test';

test('user can complete registration', async ({ page }) => {
  await page.goto('/register');

  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="password"]', 'securePassword123');
  await page.click('button[type="submit"]');

  await expect(page.locator('.success-message')).toBeVisible();
  await expect(page).toHaveURL('/dashboard');
});
```

## CI/CD Pipeline

### GitHub Actions Workflow
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck
      - run: npm run test
      - run: npm run build

  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npm run test:e2e
```

## Related Documentation

- **System Patterns**: `systemPatterns.md` - Architecture and design patterns
- **Project Brief**: `projectbrief.md` - Project goals and scope
- **Progress**: `progress.md` - Implementation status
- **AI Guide**: `AI_GUIDE.md` - Efficient AI assistant usage

---

**Navigation:** [Back to startHere.md](./startHere.md) | [System Patterns](./systemPatterns.md) | [Project Brief](./projectbrief.md)

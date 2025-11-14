# Business Processes Framework

**Purpose:** Documentation for workflows, state machines, approval chains, and multi-step business processes.

**When to use:** When designing complex workflows, documenting state transitions, planning approval chains, or defining business logic.

---

## 📁 Directory Structure

```
business-processes/
├── workflows/              # End-to-end business process flows
├── approval-chains/        # Approval routing and escalation logic
├── state-machines/         # State transition definitions and rules
└── examples/               # Example workflows and state machines
```

---

## 🎯 What to Document Here

### Workflows (`workflows/`)

Document end-to-end business processes that span multiple steps, actors, or systems.

**File naming:** `{process-name}-workflow.md` (e.g., `order-fulfillment-workflow.md`, `user-onboarding-workflow.md`)

**Template structure:**
```markdown
# [Process Name] Workflow

## Overview
Brief description of the workflow and its business purpose.

**Trigger:** What initiates this workflow?
**Actors:** Who is involved? (user roles, systems, integrations)
**Duration:** Typical time to complete
**Frequency:** How often does this occur?

## Workflow Diagram
\`\`\`mermaid
flowchart TD
    A[Start: Order Placed] --> B{Payment Valid?}
    B -->|Yes| C[Reserve Inventory]
    B -->|No| D[Reject Order]
    C --> E{Inventory Available?}
    E -->|Yes| F[Create Shipment]
    E -->|No| G[Backorder]
    F --> H[Ship Order]
    H --> I[Update Customer]
    I --> J[End: Order Fulfilled]
    G --> K[Notify Customer]
    K --> J
    D --> L[End: Order Rejected]
\`\`\`

## Detailed Steps

### Step 1: Order Placement
**Actor:** Customer
**System:** Order Service
**Actions:**
1. Customer submits order with items and payment
2. System validates order structure
3. System generates order ID
**Outputs:** Order record created with status "pending"

### Step 2: Payment Validation
**Actor:** Payment Service
**System:** Payment Gateway Integration
**Actions:**
1. Charge payment method
2. Receive payment confirmation
3. Update order with payment status
**Success:** Proceed to Step 3
**Failure:** Mark order as "payment_failed", send notification

### Step 3: Inventory Reservation
**Actor:** Inventory Service
**System:** Warehouse Management
**Actions:**
1. Check inventory availability for all items
2. Reserve inventory for order
3. Lock inventory from other orders
**Success:** Proceed to Step 4
**Failure:** Create backorder, notify customer

[Continue for all steps...]

## Business Rules

### Validation Rules
- Order total must be > $0
- All items must be valid product IDs
- Payment method must be on file
- Shipping address must be valid

### Decision Logic
- **Payment validation timeout:** 30 seconds, then retry once
- **Inventory reservation hold:** 15 minutes, then release
- **Backorder eligibility:** Only for products with restock_date set

### Error Handling
- **Payment failure:** Notify customer, hold order for 24 hours, retry
- **Inventory shortage:** Offer partial fulfillment or wait for restock
- **Shipment failure:** Retry up to 3 times, then escalate to manual

## SLAs and Metrics

### Performance Targets
- Order placement to payment validation: <5 seconds
- Payment to shipment creation: <1 hour (business hours)
- Order to shipment: <24 hours (standard shipping)

### Success Metrics
- Order completion rate: >95%
- Payment failure rate: <2%
- Inventory stockout rate: <5%

## Integration Points

### Internal Services
- **Order Service:** Order creation and management
- **Payment Service:** Payment processing
- **Inventory Service:** Inventory reservation
- **Shipment Service:** Shipping and tracking

### External Systems
- **Payment Gateway:** Stripe, PayPal
- **Shipping Provider:** USPS, FedEx, UPS
- **Email Service:** SendGrid (customer notifications)

## Data Flow

### Input Data
\`\`\`json
{
  "customer_id": "uuid",
  "items": [{"product_id": "uuid", "quantity": 1}],
  "payment_method_id": "uuid",
  "shipping_address": {...}
}
\`\`\`

### Output Data
\`\`\`json
{
  "order_id": "uuid",
  "status": "fulfilled",
  "tracking_number": "string",
  "estimated_delivery": "2025-10-20"
}
\`\`\`

## Edge Cases and Exceptions

### Partial Fulfillment
**Scenario:** Some items in stock, some backordered
**Handling:** Offer customer choice to split shipment or wait

### Payment Authorization Hold
**Scenario:** Payment authorized but not captured
**Handling:** Capture on shipment, void if order cancelled

### Address Validation Failure
**Scenario:** Shipping address invalid
**Handling:** Notify customer, hold order pending correction

## Testing Strategy

### Unit Tests
- Validate order structure
- Payment validation logic
- Inventory reservation logic

### Integration Tests
- Full order-to-shipment flow
- Payment gateway integration
- Inventory system integration

### E2E Tests
- Happy path: successful order fulfillment
- Failure path: payment decline
- Edge case: partial inventory availability

## Monitoring and Alerts

### Key Metrics to Monitor
- Order processing time (p50, p95, p99)
- Payment failure rate
- Inventory stockout incidents
- Failed shipment creation attempts

### Alert Thresholds
- Order processing time > 30 minutes: WARNING
- Payment failure rate > 5%: CRITICAL
- Inventory stockout: NOTIFY

## Rollout and Maintenance

### Deployment Considerations
- Feature flag for gradual rollout
- Backward compatibility with existing orders
- Data migration for order history

### Maintenance Schedule
- **Weekly:** Review failed orders and exceptions
- **Monthly:** Analyze performance metrics and optimize
- **Quarterly:** Update SLAs based on performance data
```

---

### Approval Chains (`approval-chains/`)

Document approval routing logic for multi-level approvals.

**File naming:** `{approval-type}-approval-chain.md` (e.g., `expense-approval-chain.md`, `purchase-order-approval-chain.md`)

**Template structure:**
```markdown
# [Approval Type] Approval Chain

## Overview
Description of what requires approval and why.

## Approval Levels

### Level 1: Manager Approval
**Triggered when:** Expense < $500
**Approvers:** Direct manager
**Timeout:** 48 hours
**On timeout:** Auto-approve if <$100, escalate to Level 2

### Level 2: Director Approval
**Triggered when:** Expense >= $500 AND < $5,000
**Approvers:** Department director
**Timeout:** 72 hours
**On timeout:** Escalate to Level 3

### Level 3: Executive Approval
**Triggered when:** Expense >= $5,000
**Approvers:** VP or above
**Timeout:** 1 week
**On timeout:** Reject and require resubmission

## Dynamic Routing Rules

### Rule 1: Department-Specific Routing
\`\`\`javascript
if (expense.department === "IT" && expense.amount < $10000) {
  approvers = [CIO];
} else if (expense.amount >= $10000) {
  approvers = [CFO, CEO];
}
\`\`\`

### Rule 2: Type-Based Routing
- **Travel expenses:** Travel coordinator → Manager → Director
- **Capital expenses:** Finance team → CFO → Board (if > $50k)
- **Software subscriptions:** IT security → IT manager → CIO

## Escalation Procedures

### Automatic Escalation
- After timeout, escalate to next level
- Send notification to original approver
- Log escalation reason

### Manual Escalation
- Submitter can request escalation with justification
- Manager can escalate urgent requests
- Finance team can escalate compliance issues

## Notification Templates

### Approval Request
**Subject:** Expense Approval Needed: [Expense Title] - $[Amount]
**Body:** [Submitter] has submitted an expense for $[Amount]. Review and approve/reject.

### Approval Granted
**Subject:** Expense Approved: [Expense Title]
**Body:** Your expense has been approved by [Approver]. Next steps: [Actions]

### Approval Rejected
**Subject:** Expense Rejected: [Expense Title]
**Body:** Your expense was rejected by [Approver]. Reason: [Rejection Reason]

## Audit Requirements
- Log all approval actions (approve, reject, escalate)
- Track approval timestamps and approver identity
- Maintain approval chain history for compliance
- Generate approval reports for finance team
```

---

### State Machines (`state-machines/`)

Document formal state transitions and business rules.

**File naming:** `{entity}-state-machine.md` (e.g., `order-state-machine.md`, `user-state-machine.md`)

**Template structure:**
```markdown
# [Entity] State Machine

## State Diagram
\`\`\`mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Submitted: submit()
    Submitted --> InReview: assign_reviewer()
    InReview --> Approved: approve()
    InReview --> Rejected: reject()
    InReview --> NeedsRevision: request_changes()
    NeedsRevision --> Submitted: resubmit()
    Approved --> Published: publish()
    Published --> Archived: archive()
    Rejected --> [*]
    Archived --> [*]
\`\`\`

## States

### Draft
**Description:** Initial state, editable by creator
**Allowed actions:** edit, delete, submit
**Transitions:**
- `submit()` → Submitted (requires validation)

### Submitted
**Description:** Submitted for review, read-only
**Allowed actions:** view, assign_reviewer, withdraw
**Transitions:**
- `assign_reviewer()` → InReview
- `withdraw()` → Draft

### InReview
**Description:** Under active review
**Allowed actions:** approve, reject, request_changes, comment
**Transitions:**
- `approve()` → Approved (requires reviewer permission)
- `reject()` → Rejected (requires reason)
- `request_changes()` → NeedsRevision

### NeedsRevision
**Description:** Changes requested, editable by creator
**Allowed actions:** edit, resubmit
**Transitions:**
- `resubmit()` → Submitted

### Approved
**Description:** Approved, ready for publication
**Allowed actions:** publish, unapprove
**Transitions:**
- `publish()` → Published

### Published
**Description:** Live and visible to users
**Allowed actions:** view, archive
**Transitions:**
- `archive()` → Archived

### Rejected
**Description:** Rejected, final state
**Allowed actions:** view
**Transitions:** None (terminal state)

### Archived
**Description:** Archived, preserved for history
**Allowed actions:** view, restore
**Transitions:**
- `restore()` → Published (admin only)

## Transition Rules

### Validation Rules
**submit():**
- All required fields must be filled
- Content must pass validation checks
- Creator must have submit permission

**approve():**
- User must have reviewer role
- Review must be assigned to approver
- No blocking comments unresolved

**publish():**
- Must be in Approved state
- Publish date/time must be set
- All dependencies must be published

### Permission Requirements
| Action | Required Permission |
|--------|---------------------|
| submit | creator or editor |
| assign_reviewer | editor or admin |
| approve | reviewer or admin |
| reject | reviewer or admin |
| publish | publisher or admin |
| archive | admin |

## Event Logging
Log all state transitions with:
- Timestamp
- Actor (user who triggered transition)
- Previous state
- New state
- Transition action
- Metadata (e.g., rejection reason, approval notes)

## Notifications
- **Draft → Submitted:** Notify editors and reviewers
- **Submitted → InReview:** Notify assigned reviewer
- **InReview → Approved:** Notify creator and publisher
- **InReview → Rejected:** Notify creator with reason
- **Approved → Published:** Notify all stakeholders
```

---

## 🎓 Best Practices

### 1. Workflow Documentation
- **Use visual diagrams** - Flowcharts and sequence diagrams are clearer than text
- **Document decision points** - Explain why the workflow branches
- **Include timings** - SLAs and expected durations for each step
- **Link to code** - Reference implementation in codebase

### 2. Approval Chain Design
- **Keep it simple** - Minimize approval levels
- **Set clear thresholds** - Dollar amounts, risk levels, etc.
- **Handle timeouts** - Always define timeout behavior
- **Allow escalation** - Both automatic and manual

### 3. State Machine Clarity
- **Define all states** - Even temporary or error states
- **Document transitions** - What triggers each transition
- **Enforce permissions** - Who can trigger which transitions
- **Log everything** - Audit trail is critical for state machines

---

## 🔄 Related Documentation

### Memory-Bank References
- `memory-bank/data-architecture/` - Data models for workflow entities
- `memory-bank/security-compliance/` - Access control for workflows
- `memory-bank/integrations/` - External system integrations in workflows

---

**Last Updated:** 2025-10-14
**Maintainer:** Development Team
**Review Frequency:** Monthly (or on process changes)

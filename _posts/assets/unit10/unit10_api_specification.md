# Unit 10 Artefact – API Security Requirements Specification  
**Project Context: Electricity Billing Data API**

This document defines the security requirements for an API that transfers electricity billing data between a Python analytics application and a relational SQL backend database. The API processes personal and operational datasets including:

- Customer profiles (name, address, account ID)  
- Energy consumption metrics  
- Meter readings  
- Invoicing and payment records

Because these datasets contain personally identifiable information (PII), controls were designed to ensure confidentiality, integrity, availability and regulatory compliance in line with GDPR requirements and industry API security practices.

---

## 1. Authentication & Access Control

### 1.1 Identity Management
- **OAuth 2.0 token-based authentication** is used to authenticate clients without exposing permanent credentials.
- Tokens are:
  - Time-limited.
  - Scope-restricted.
  - Revocable if compromised.

### 1.2 Role-Based Access Control

API access is segmented by role:

| Role                    | Permitted Actions                      |
|--------------------------|------------------------------------------|
| Meter Ingestion Service | Submit new meter readings only           |
| Billing Engine          | Generate and update bills                |
| Analytics Application  | Read-only access to aggregated datasets  |
| Support Dashboard      | Limited customer data lookup             |

No role has unrestricted database access.

---

## 2. Safe Data Parsing

### 2.1 JSON Validation
All inbound JSON payloads must comply with approved schemas:

- Field types enforced
- Length constraints applied
- Mandatory field checking
- Rejection of unknown parameters

Malformed or oversized payloads are rejected with **HTTP 400 errors** prior to database processing.

### 2.2 XML Processing Controls

When handling XML:

- External entities and expansion features are disabled.
- Document size and recursion depth limits are enforced.
- Valid schemas are required before parsing occurs.

This prevents **XXE injection** and parser exploitation attacks.

### 2.3 SQL Injection Protection

All database interactions use:

- **Prepared SQL statements**
- Bound parameters only
- No dynamic query string concatenation

This ensures user input cannot modify query structure or manipulate database execution.

---

## 3. Abuse Prevention

To reduce misuse or large-scale data extraction:

### 3.1 Rate Limiting
- Per-token request limits enforced.
- Excess traffic triggers HTTP 429 responses.

### 3.2 Pagination Controls
- Result sets are restricted to page-based responses.
- Bulk data export endpoints are disabled by default.

### 3.3 Account Lockout Policies
- Repeated authentication failures result in:
  - Temporary client blocking.
  - Automated breach alerts.

---

## 4. Logging & Monitoring

### 4.1 Activity Logging
- All API requests logged with:
  - Timestamp
  - Client ID
  - Endpoint ID
  - Response status

No personal data values are written to logs.

### 4.2 Behavioural Monitoring

Automated alerts trigger on:

- Unusual query volumes.
- Access attempts outside expected hours.
- Endpoint scanning behaviour.

---

## 5. Transmission & Storage Security

### 5.1 Transport Encryption
- Mandatory **TLS 1.2+ (HTTPS)** encryption for all endpoints.
- No plaintext traffic permitted.

### 5.2 Data-at-Rest Protection
- Database-level encryption applied to PII fields.
- Encrypted backups maintained.
- Access governed by server RBAC.

---

## 6. Error Handling

Error messages must:

- Never expose SQL statements.
- Never identify table names or schema structure.
- Provide only minimal failure information.

Example acceptable response:
```json
{
  "error": "Invalid request parameters."
}

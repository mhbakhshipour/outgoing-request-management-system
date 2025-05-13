### Task: Outgoing Request Management System

**Objective:**  
Design and implement a system to manage outgoing requests to third-party providers, adhering to their specific rate limits and ensuring the processing order is maintained for each provider.

---

### Problem Description:

#### Providers and Rate Limits:
- The system involves **N providers (P1 to PN)**, each offering exactly one API.
- Each provider has a **unique API interface** (e.g., different endpoints, request/response formats, or authentication mechanisms). However, the schema of the incoming messages to the system is the same for all providers.
- Each provider has a **rate limit** that determines the number of requests it can handle per second.

#### Request Generation:
- Requests are generated dynamically. For example:
  - When a user clicks a button.
  - When an event is triggered by another service.
- Requests must be processed in the **order they occur** for each provider.

#### Incoming Requests:
- The average incoming request rate is about **100 requests per second**.
- Each request is **specific to a provider** (e.g., a request for P1 cannot be processed by P2).

---

### Processing Example:

If:
- **P1** accepts **0.2 requests/second** (1 request every 5 seconds).
- **P2** accepts **0.1 requests/second** (1 request every 10 seconds).

Requests would be processed as follows:
- **R1** for P1 at t=1 is processed immediately.
- **R2** for P1 at t=6 (next available time).
- **R3** for P2 at t=5 is processed immediately.
- **R4** for P2 at t=15.
- **R5** for P1 at t=11.

---

### Task Requirements:

#### System Design:
- Accept input/configuration for:
  - The number of providers.
  - Their respective rate limits (requests per second).
  - The unique API interface details for each provider (e.g., endpoint, authentication, etc.).
- Ensure that the system can handle **provider-specific APIs** while maintaining a consistent message schema for incoming requests.

#### Constraints:
- Do not use a database to store or query requests.
- Requests must be processed in **real-time** based on provider availability.
- The system must respect the **unique API interfaces** of each provider.

---

### Bonus Points:

You may implement the following optional features for additional credit:

#### Request Prioritization:
- Assign a **priority** to each request.
- When multiple requests are waiting, process the one with the **highest priority** first.

#### Provider Management:
- Allow providers to be **toggled on or off dynamically** (provide an interface depending on your decision).
- A provider cannot process requests while it is off.

#### Execution Time:
- Include an **execution time** for each request.
- A request should be processed only at or after its execution time.

---

### Guidelines:
- You are not required to handle incoming/outgoing requests as HTTP requests. Simulating them as function calls is sufficient.
- Use **Python** (recommended and is a plus, but not mandatory).
- If you have questions or wish to use a specific library, feel free to ask.
- A simple script is sufficient for this task.

---

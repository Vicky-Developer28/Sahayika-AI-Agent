Hackathon Analysis Skill

1. Skill Name

Hackathon Analysis

2. Purpose

This skill performs a complete analysis of a hackathon before implementation begins.

The skill must transform a raw hackathon announcement, problem statement, theme, requirements, constraints, or challenge description into a detailed:

HackathonAnalysis.md

The analysis must help the development team understand:

- What the hackathon is asking for
- What problem needs to be solved
- Who has the problem
- What the expected solution should accomplish
- Functional and non-functional requirements
- Constraints and assumptions
- Technical opportunities
- Risks
- MVP scope
- Possible architecture
- Technology choices
- Development priorities
- Testing requirements
- Demonstration strategy
- Evaluation considerations
- Future improvements

This skill performs analysis only unless implementation is explicitly requested.

---

3. Input Arguments

The skill may receive the following arguments.

Hackathon Name:
Hackathon Organizer:
Problem Statement:
Challenge Description: 
Theme:
Programming Language:
Framework:
Development Time:
Team Size:
Target Platform:
Required Technologies:
Preferred Technologies:
Restrictions:
Judging Criteria:
Submission Requirements:
Additional Information:

Required Input

At minimum, one of the following must be provided:

- Hackathon problem statement
- Challenge description
- Hackathon theme
- Competition requirements

Optional Input

If information is missing, do not invent it.

Mark it as:

Not Provided

or:

To Be Confirmed

---

4. Core Principles

The analysis must follow these principles.

4.1 Do Not Invent Requirements

Never assume that an unstated requirement is mandatory.

Clearly distinguish between:

- Explicit Requirement
- Strongly Implied Requirement
- Recommended Feature
- Optional Feature
- Assumption

---

4.2 Separate Facts From Recommendations

Use separate sections for:

Given Information
Analysis
Recommendation
Assumption
Risk

Do not present recommendations as requirements.

---

4.3 Prioritize the Problem

Do not immediately choose technologies.

First understand:

Problem
↓
Users
↓
Pain Point
↓
Objective
↓
Requirements
↓
Solution
↓
Architecture
↓
Technology

---

4.4 Optimize for Hackathon Reality

The analysis must consider:

- Limited development time
- Team size
- Developer experience
- Integration complexity
- Deployment difficulty
- Testing time
- Presentation/demo time
- Reliability
- Scope creep

A technically impressive feature that cannot be completed reliably within the available time should be classified appropriately.

---

5. Analysis Workflow

Step 1 — Parse the Hackathon

Extract:

- Hackathon name
- Organizer
- Theme
- Domain
- Problem statement
- Target users
- Submission requirements
- Constraints
- Judging criteria
- Timeline

Create a structured understanding before continuing.

---

Step 2 — Analyze the Problem Statement

Break the problem statement into:

Actual Problem Statement

Preserve the original statement as provided.

Simple English Explanation

Explain the problem in simple language.

Core Problem

Identify the central problem that must be solved.

Root Problem

Identify the underlying reason the problem exists when it can be determined from the provided information.

Symptoms

Identify observable problems caused by the core problem.

Consequences

Explain what happens if the problem remains unsolved.

---

Step 3 — Problem Decomposition

Break the problem into smaller problems.

Example:

Main Problem
├── Problem A
│   ├── Sub-problem A1
│   └── Sub-problem A2
├── Problem B
│   ├── Sub-problem B1
│   └── Sub-problem B2
└── Problem C

For every major sub-problem identify:

- Description
- Cause
- Impact
- Possible solution
- Priority

---

Step 4 — Identify Stakeholders

Identify relevant stakeholders.

Possible categories:

- Primary users
- Secondary users
- Administrators
- Organizations
- Service providers
- Developers
- Government bodies
- Businesses
- Communities

For each stakeholder explain:

Stakeholder
Problem
Need
Expected Benefit

Do not invent stakeholders without explaining why they are relevant.

---

Step 5 — Target Users

Define:

Primary Target Users

Users directly affected by the problem.

Secondary Target Users

Users indirectly affected.

System Administrators

People responsible for managing the system.

For each user type identify:

- Goals
- Problems
- Needs
- Expected interaction
- Technical capability

---

Step 6 — Objectives

Extract the objectives.

Separate them into:

Primary Objectives

Objectives explicitly required by the challenge.

Secondary Objectives

Objectives that support the primary goal.

Optional Objectives

Potential improvements that are not required for the MVP.

---

Step 7 — Requirements Analysis

Create a complete requirements breakdown.

Functional Requirements

Identify what the system must do.

Example:

FR-01 — User Registration
FR-02 — User Authentication
FR-03 — Data Collection
FR-04 — Data Processing
FR-05 — Dashboard

Each requirement should contain:

ID
Name
Description
Priority
Source
Dependencies

Priority:

Critical
High
Medium
Low
Optional

---

Non-Functional Requirements

Analyze:

- Performance
- Security
- Scalability
- Availability
- Reliability
- Maintainability
- Accessibility
- Usability
- Privacy
- Compatibility

Do not mark a requirement as mandatory unless supported by the problem statement or submission requirements.

---

Step 8 — Constraints

Identify all constraints.

Time Constraints

Analyze the available development time.

Team Constraints

Consider:

- Team size
- Skill distribution
- Parallel development

Technical Constraints

Consider:

- Required language
- Required framework
- APIs
- Hardware
- Platform
- Internet dependency
- Third-party services

Submission Constraints

Consider:

- Repository
- Documentation
- Demo
- Video
- Presentation
- Deployment URL
- Source code

---

Step 9 — Assumptions

Create an explicit assumption list.

Format:

A-01:
Assumption

Reason:
Why this assumption is being made.

Risk:
What happens if it is incorrect.

Never hide assumptions inside the architecture.

---

Step 10 — Solution Analysis

Describe potential solution approaches.

For each approach:

Approach
Description
Advantages
Disadvantages
Complexity
Hackathon Feasibility
Dependencies
Risks

Do not select a solution purely because it uses newer or more complex technology.

---

Step 11 — MVP Definition

Define the smallest useful working solution.

Classify features as:

Must Have

Required for a meaningful submission.

Should Have

Important but not absolutely necessary.

Could Have

Useful improvements.

Won't Have

Features intentionally excluded from the MVP.

Use:

MVP
├── Must Have
├── Should Have
├── Could Have
└── Won't Have

---

Step 12 — Feature Prioritization

Create a feature matrix.

Feature| User Value| Technical Complexity| Priority| MVP
Feature A| High| Medium| Critical| Yes
Feature B| High| High| High| Yes
Feature C| Medium| High| Medium| No

Do not assign arbitrary numerical scores unless useful.

---

Step 13 — User Flow

Describe the complete user journey.

Example:

User
 ↓
Landing Page
 ↓
Authentication
 ↓
Input
 ↓
Processing
 ↓
Result
 ↓
Action
 ↓
Confirmation

Identify:

- Entry point
- User actions
- System responses
- Error states
- Completion state

---

Step 14 — System Flow

Describe the internal system flow.

Example:

Client
 ↓
Frontend
 ↓
API
 ↓
Authentication
 ↓
Business Logic
 ↓
Database
 ↓
External Service
 ↓
Response
 ↓
Frontend

---

Step 15 — Data Flow

Identify:

- Input data
- Data validation
- Data processing
- Storage
- Retrieval
- Output
- External data sources

Create a conceptual data-flow diagram using Mermaid where appropriate.

---

Step 16 — Architecture Analysis

Propose an architecture appropriate to the problem.

Consider:

- Frontend
- Backend
- Database
- Authentication
- APIs
- External services
- Background jobs
- File storage
- Caching
- Monitoring

Keep architecture proportional to the hackathon.

Do not introduce microservices unless there is a clear reason.

---

Step 17 — Technology Analysis

Analyze possible technologies.

The skill may consider:

Languages

- Rust
- Python
- C
- Lua

Web

- Django
- Axum
- Actix
- Dioxus
- Yew
- HTMX

Database

Choose according to requirements, such as:

- PostgreSQL
- SQLite
- MySQL
- Redis

Do not automatically use every technology listed above.

Technology selection must be based on:

Requirement
→ Technical Need
→ Technology Capability
→ Development Speed
→ Reliability
→ Team Skill

---

Step 18 — Technology Recommendation

For each major technology provide:

Technology:
Purpose:
Why It Fits:
Advantages:
Limitations:
Alternative:
Decision:

The recommendation must be justified by the hackathon requirements.

---

Step 19 — Database Analysis

Identify required entities.

Example:

User
Project
Submission
Event
Notification

For each entity identify:

- Fields
- Relationships
- Primary key
- Foreign keys
- Constraints

Generate an ER diagram when appropriate.

---

Step 20 — API Analysis

Identify required APIs.

Example:

POST /api/auth/register
POST /api/auth/login
GET  /api/user
POST /api/data
GET  /api/dashboard

For each API document:

Method
Endpoint
Purpose
Authentication
Request
Response
Errors

Do not invent API endpoints when they are not relevant.

---

Step 21 — Security Analysis

Analyze:

- Authentication
- Authorization
- Input validation
- SQL injection
- XSS
- CSRF
- Rate limiting
- Secrets management
- API security
- File upload security
- Data privacy
- Logging
- Dependency security

For sensitive systems, identify additional domain-specific security concerns.

---

Step 22 — Privacy Analysis

Identify:

- Personal data
- Sensitive data
- Data collection
- Data storage
- Data retention
- Data sharing
- User consent
- Data deletion

If privacy requirements are unknown, mark them as requiring confirmation.

---

Step 23 — Performance Analysis

Identify potential bottlenecks.

Consider:

- CPU
- Memory
- Network
- Database
- API latency
- Large datasets
- Concurrent users
- File processing

Define realistic optimization priorities.

Avoid premature optimization.

---

Step 24 — Testing Strategy

Define:

Unit Testing

Test individual components.

Integration Testing

Test interactions between components.

End-to-End Testing

Test complete user flows.

Security Testing

Test security-critical functionality.

Performance Testing

Test important performance requirements.

---

Step 25 — Risk Analysis

Create a risk table.

Risk| Probability| Impact| Mitigation
API failure| Medium| High| Fallback
Time shortage| High| High| MVP-first
Integration issue| Medium| High| Early integration

Also identify:

- Technical risks
- Schedule risks
- Team risks
- Dependency risks
- Deployment risks
- Demo risks

---

Step 26 — Dependency Analysis

Identify:

- External APIs
- SDKs
- Libraries
- Cloud services
- Authentication providers
- Databases
- Hardware
- Internet connectivity

For each dependency determine:

Required?
Alternative?
Failure impact?
Local fallback?

---

Step 27 — Development Plan

Create a development sequence.

Example:

Phase 1 — Project Setup
Phase 2 — Core Backend
Phase 3 — Database
Phase 4 — Frontend
Phase 5 — Integration
Phase 6 — Testing
Phase 7 — Deployment
Phase 8 — Demo Preparation

Prioritize vertical slices over building every layer independently.

---

Step 28 — Time Allocation

Use the provided development time.

Example:

10 hours total

Planning       0.5h
Architecture   0.5h
MVP Backend    2.0h
MVP Frontend   2.0h
Integration    2.0h
Testing        1.0h
Deployment     0.5h
Demo           1.0h
Buffer         0.5h

The actual allocation must depend on the project.

Always reserve time for:

- Integration
- Testing
- Deployment
- Demo
- Unexpected problems

---

Step 29 — Team Responsibilities

If team size is provided, divide responsibilities.

Example:

Developer 1
→ Backend + API

Developer 2
→ Frontend

Developer 3
→ Database + Integration

Developer 4
→ Testing + Deployment + Documentation

Avoid creating unnecessary parallel work.

---

Step 30 — Demo Strategy

Analyze how the solution should be demonstrated.

The demo should show:

Problem
↓
Current Pain
↓
Solution
↓
Core Feature
↓
Real User Flow
↓
Result
↓
Impact

Identify the shortest reliable path to demonstrate the core value.

---

Step 31 — Presentation Structure

Generate a recommended presentation structure:

1. Problem
2. Existing Situation
3. Proposed Solution
4. Target Users
5. Key Features
6. User Flow
7. Architecture
8. Technology
9. Security
10. Demo
11. Expected Impact
12. Future Improvements

Do not claim that these are official judging requirements unless explicitly provided.

---

Step 32 — Evaluation Criteria Analysis

If official judging criteria are provided, analyze each criterion.

For each criterion:

Criterion
Official Requirement
What It Means
Relevant Features
Evidence to Demonstrate

If judging criteria are not provided:

Official judging criteria were not provided.
Do not assume unofficial criteria are mandatory.

Possible areas to analyze separately include:

- Problem relevance
- Functionality
- Technical implementation
- Usability
- Innovation
- Impact
- Presentation

These must be labeled as potential evaluation considerations, not official criteria.

---

Step 33 — Competitive / Existing Solution Analysis

If information about existing solutions is available, analyze:

Existing Solution
What It Does
Strengths
Limitations
Gap
Proposed Differentiation

Do not make unsupported claims about competitors.

---

Step 34 — Innovation Analysis

Identify possible areas of differentiation.

Examples:

- Better workflow
- Lower cost
- Better accessibility
- Faster processing
- Offline capability
- Automation
- Better UX
- Privacy
- Reliability
- Integration

Do not claim something is "innovative" merely because it uses a particular technology.

Explain what differentiates it.

---

Step 35 — Failure Scenarios

Identify what can go wrong.

Example:

User Input Failure
API Failure
Database Failure
Network Failure
Authentication Failure
External Service Failure
Invalid Data
System Overload
Deployment Failure

For important failures specify:

Detection
Response
Fallback
User Message
Recovery

---

Step 36 — Future Scope

Separate future features from MVP features.

MVP
→ Required for hackathon

Post-Hackathon
→ Features that can be developed later

Do not allow future scope to expand the MVP unnecessarily.

---

Step 37 — Final Feasibility Analysis

Evaluate feasibility using descriptive categories:

Development Complexity:
Low / Medium / High

Integration Complexity:
Low / Medium / High

Deployment Complexity:
Low / Medium / High

Time Pressure:
Low / Medium / High

Technical Risk:
Low / Medium / High

Overall Scope:
Small / Medium / Large

Explain the reason for each classification.

Do not provide arbitrary numerical scores unless explicitly requested.

---

6. Required Output

The skill must generate:

HackathonAnalysis.md

The generated document must follow this structure:

# Hackathon Analysis

## 1. Hackathon Overview

## 2. Problem Statement

### 2.1 Actual Problem Statement
### 2.2 Simple English Explanation
### 2.3 Core Problem
### 2.4 Root Problem
### 2.5 Symptoms
### 2.6 Consequences

## 3. Problem Breakdown

## 4. Stakeholders

## 5. Target Users

## 6. Objectives

### 6.1 Primary Objectives
### 6.2 Secondary Objectives
### 6.3 Optional Objectives

## 7. Requirements

### 7.1 Functional Requirements
### 7.2 Non-Functional Requirements

## 8. Constraints

## 9. Assumptions

## 10. Solution Analysis

## 11. Proposed Solution

## 12. MVP

### 12.1 Must Have
### 12.2 Should Have
### 12.3 Could Have
### 12.4 Won't Have

## 13. Feature Prioritization

## 14. User Flow

## 15. System Flow

## 16. Data Flow

## 17. Architecture

## 18. Technology Analysis

## 19. Technology Recommendation

## 20. Database Design

## 21. API Design

## 22. Security Analysis

## 23. Privacy Analysis

## 24. Performance Analysis

## 25. Testing Strategy

## 26. Risk Analysis

## 27. Dependencies

## 28. Development Plan

## 29. Time Allocation

## 30. Team Responsibilities

## 31. Demo Strategy

## 32. Presentation Structure

## 33. Evaluation Criteria Analysis

## 34. Existing Solution Analysis

## 35. Innovation Analysis

## 36. Failure Scenarios

## 37. Future Scope

## 38. Feasibility Analysis

## 39. Final Recommendations

## 40. Final Checklist

---

7. Mermaid Diagrams

Use Mermaid diagrams when they improve understanding.

Possible diagrams:

flowchart TD
    A[User] --> B[Frontend]
    B --> C[Backend API]
    C --> D[Business Logic]
    D --> E[Database]

Possible diagram types:

- Flowchart
- Sequence diagram
- ER diagram
- Architecture diagram
- User journey

Do not generate diagrams merely for decoration.

---

8. Source and Evidence Rules

When external information is used:

- Identify the source.
- Prefer official hackathon documentation.
- Prefer official technology documentation.
- Distinguish provided information from researched information.
- Do not present assumptions as facts.
- Do not fabricate sources.

If web research is available and current information is necessary, verify important claims before including them.

---

9. Decision Rules

When choosing between technologies:

Requirement
↓
Constraint
↓
Team Capability
↓
Development Time
↓
Reliability
↓
Security
↓
Performance
↓
Maintainability
↓
Technology Choice

Do not choose technology based solely on popularity.

---

10. Scope Control

The skill must actively prevent scope creep.

When a feature is proposed, classify it:

Required for MVP
Useful but Non-Essential
Post-Hackathon
Out of Scope

If a feature significantly increases development complexity without being necessary for the core problem, recommend moving it outside the MVP.

---

11. Unknown Information

If information is missing:

> **Information Gap**
>
> This information was not provided in the hackathon description.
> It should be confirmed before implementation.

Never silently fill important missing information.

---

12. Final Checklist

Before generating "HackathonAnalysis.md", verify:

- [ ] Hackathon information extracted
- [ ] Problem statement understood
- [ ] Problem decomposed
- [ ] Target users identified
- [ ] Objectives identified
- [ ] Functional requirements identified
- [ ] Non-functional requirements identified
- [ ] Constraints identified
- [ ] Assumptions documented
- [ ] MVP defined
- [ ] Features prioritized
- [ ] User flow defined
- [ ] System flow defined
- [ ] Data flow defined
- [ ] Architecture analyzed
- [ ] Technology options analyzed
- [ ] Technology recommendation justified
- [ ] Database requirements analyzed
- [ ] API requirements analyzed
- [ ] Security analyzed
- [ ] Privacy analyzed
- [ ] Performance analyzed
- [ ] Testing strategy defined
- [ ] Risks identified
- [ ] Dependencies identified
- [ ] Development plan created
- [ ] Time allocation created
- [ ] Team responsibilities defined
- [ ] Demo strategy created
- [ ] Presentation structure created
- [ ] Official judging criteria analyzed if available
- [ ] Existing solutions analyzed if relevant
- [ ] Innovation opportunities identified
- [ ] Failure scenarios analyzed
- [ ] Future scope separated from MVP
- [ ] Feasibility analyzed
- [ ] Information gaps clearly marked
- [ ] No unsupported requirements invented

---

13. Completion Condition

The skill is complete only when:

1. The entire hackathon problem has been analyzed.
2. Requirements are clearly separated from assumptions.
3. The MVP is clearly defined.
4. Technical decisions are justified.
5. Risks and constraints are documented.
6. Development can begin using the analysis.
7. The final document is saved as:

HackathonAnalysis.md

The analysis must be detailed enough that a development team can use it as the primary planning document before creating the actual project arPychitecture and source code.
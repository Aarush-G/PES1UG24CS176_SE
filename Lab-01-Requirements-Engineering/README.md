# Lab 01 — Requirements Engineering & UML Use-Case Modelling

## Problem Statement #47

### Domain & SSL Certificate Expiry Alert System

An IT operations utility that performs automated daily WHOIS registration and SSL/TLS handshake audits, alerting system administrators through escalation ladders before domain or certificate expiration.

## Objective

The objective of this lab is to elicit and document functional and non-functional requirements from a given scenario and translate them into a UML use-case diagram and a use-case flow specification.

## Actors

* **SysAdmin**
* **Security Officer**
* **WHOIS Service**

## Key Use Cases

* **UC-01:** Manage Monitored Domains
* **UC-02:** Run Daily Domain Audit
* **UC-03:** Perform WHOIS Check
* **UC-04:** Perform SSL/TLS Audit
* **UC-05:** Generate Expiry Alert
* **UC-06:** Escalate Alert
* **UC-07:** View Audit Results

## Requirements

The requirements table contains:

* **5 Functional Requirements (FR-001 to FR-005)**
* **2 Non-Functional Requirements (NFR-001 and NFR-002)**
* Priority, acceptance criteria, and rationale for each requirement

## UML Use-Case Model

The UML use-case diagram models the interactions between the identified actors and the Domain & SSL Certificate Expiry Alert System.

The diagram includes both:

* `«include»` relationships
* `«extend»` relationship

## Use-Case Flow

The selected core use case is:

**UC-02 — Run Daily Domain Audit**

The flow specification contains:

* Preconditions
* Postconditions
* Main Success Scenario
* Alternate Flow for an unreachable SSL/TLS endpoint

## Deliverables

| Deliverable          | File                                                                           |
| -------------------- | ------------------------------------------------------------------------------ |
| Requirements Table   | [`Requirements_Table.pdf`](./Requirements/Requirements_Table.pdf)              |
| UML Use-Case Diagram | [`Use_Case_Diagram.pdf`](./UML/Use_case_diagram.pdf)                           |
| Editable UML Diagram | [`Use_Case_Diagram.drawio`](./UML/Use_case_diagram.drawio)                     |
| Use-Case Flow        | [`UC-02_Daily_Domain_Audit.pdf`](./Use-CaseFlow/UseCaseFlowSpecification.pdf)  |

## Tools Used

* Draw.io / diagrams.net
* Microsoft Word
* GitHub

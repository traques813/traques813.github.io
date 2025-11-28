---
layout: post
title: "Project Evaluation – From Proposal to Implementation"
subtitle: "Comparing the Unit 6 design phase to the Unit 11 transactional system"
categories: project-evaluation
tags: [unit6, unit11, evaluation, database-design, transactions, c]
---

## Overview

This evaluation compares the **initial conceptual proposal developed in Unit 6** with the **final transactional database implementation delivered in Unit 11**, reflecting on how design intentions developed into a functioning system and where theoretical assumptions were refined through practical application.

The project centred on an **Electricity Bill Management System (EBMS)** designed to manage customer profiles, meter readings, billing records and payment transactions within a relational database environment.

---

## Unit 6 – Initial Proposal

The Unit 6 proposal focused primarily on **conceptual database design**. Key tasks included:

- Identifying core system entities (e.g., Customer, Meter, Reading, Bill, Payment)
- Defining relationships using ER modelling
- Applying **first to third normal form (1NF–3NF)** to remove redundancy and update anomalies
- Selecting an appropriate RDBMS platform

At this stage, the rationale for using a **relational model** was grounded in its capacity to maintain structural consistency and support transactional workloads typical of billing systems (Harrington, 2016; Date, 2013). PostgreSQL was selected conceptually due to its robustness, scalability and compliance features.

However, the proposal remained **largely theoretical**. While normalisation was demonstrated successfully at the schema level, limited attention was initially given to:

- The **operational lifecycle of transactions**
- Concurrency management when multiple users interact with records
- System response to **partial failures or rollbacks**
- Enforcement of integrity beyond static key constraints

Feedback later confirmed that the report structure diminished clarity, particularly by discussing DBMS selection before presenting the logical model, and by offering limited alignment between theoretical comparison (SQL vs NoSQL) and the specific project use case.

---

## Unit 11 – Final Implementation

Unit 11 marked a shift from design reasoning to **system execution**. The focus moved beyond static schema modelling toward ensuring the runtime reliability of the EBMS.

Using **SQLite**, the team implemented:

- Fully normalised tables with primary and foreign key constraints
- Referential integrity enforcement via explicit constraint testing
- Transaction execution scripts modelling real billing operations
- Validation through **failure injection tests** (invalid deletes, broken references)

This phase reinforced the necessity of **ACID compliance** — particularly atomicity and consistency — to ensure that financial transactions would either fully commit or leave the database unchanged (Gray and Reuter, 1993; Connolly and Begg, 2015).

Concurrency issues discussed in theory during Unit 9 became tangible when examining how partial reads or overlapping updates could corrupt totals if isolation boundaries were not respected. The importance of transaction managers, staged commits and locking behaviour became practically meaningful rather than abstract concepts.

Unit 11 also expanded understanding of **system resilience**. Logging, checkpoint logic, rollback recovery and commit durability were no longer conceptual constructs but seen as integral safeguards ensuring that service interruptions would not compromise billing accuracy (Elmasri and Navathe, 2016).

---

## Key Differences and Learning Development

The comparison between Units 6 and 11 highlights a significant evolution in technical thinking:

| Aspect | Unit 6 – Proposal | Unit 11 – Implementation |
|-------|-------------------|---------------------------|
| Focus | Logical schema design | Transaction reliability and recovery |
| Modelling | ER diagrams and normalisation | Physical tables and constraint testing |
| Integrity | Structural enforcement (keys) | Runtime enforcement (ACID controls) |
| Risk Awareness | Minimal | Explicit acknowledgement of concurrency and failure risks |
| Evaluation | Theoretical comparison | Empirical system testing |

The learning change was particularly evident in the understanding that **normalisation alone cannot guarantee system integrity**. While 3NF eliminates redundancy, transactional consistency requires additional runtime safeguards — logging mechanisms, isolation policies and rollback strategies — none of which are addressed by schema design alone (Gray and Reuter, 1993).

Unit 11 demonstrated that data correctness is maintained not only by how tables are structured but by how **operations across those tables are sequenced and protected**.

---

## Reflection on Tutor Feedback

Initial feedback noted that the proposal remained overly theoretical, particularly where comparative discussion (SQL vs NoSQL) lacked alignment with the real operational constraints of utility billing systems. Revisiting this feedback after Unit 11 clarified its relevance: the later implementation phase naturally centred the discussion on **use-case requirements**, including auditability, transactional certainty and regulatory consistency — characteristics poorly supported by most NoSQL environments (Meier and Kaufmann, 2019).

Where the proposal remained high-level, the implementation forced engagement with practical limitations. This helped close the gap between academic description and technical reasoning grounded in the system’s actual functional demands.

---

## Overall Evaluation

The shift from Unit 6 to Unit 11 reflects a clear progression from **theoretical schema modelling** to **operational systems engineering**. While the proposal effectively captured structural principles, it underestimated the importance of transaction processing and failure recovery to real-world database integrity. Unit 11 demonstrated how these runtime considerations complete the relational model by supplying the mechanisms needed to maintain trust in the data under realistic working conditions.

This progression strengthened the overall quality of the project, aligning conceptual understanding with applied system requirements and reinforcing that effective database design must be evaluated by **how systems behave under real operational pressures rather than by schema quality alone**.

---

## References (Harvard Style)

Connolly, T. and Begg, C. (2015) *Database Systems: A Practical Approach to Design, Implementation and Management*. 6th edn. Pearson.

Date, C.J. (2013) *Relational Database: Selected Writings*. Addison-Wesley.

Elmasri, R. and Navathe, S. (2016) *Fundamentals of Database Systems*. 7th edn. Pearson.

Gray, J. and Reuter, A. (1993) *Transaction Processing: Concepts and Techniques*. Morgan Kaufmann.

Harrington, J.L. (2016) *Relational Database Design and Implementation*. 4th edn. Morgan Kaufmann.

Meier, A. and Kaufmann, M. (2019) *SQL & NoSQL Databases*. Springer Vieweg.

---
layout: post
title: "Reflective Learning Review"
subtitle: "Personal and academic development across the data wrangling module"
categories: reflection
tags: [reflection, professional-development, c]
---

## Reflection on Learning and Development

When beginning this module, the subject area represented a significant shift from existing academic strengths. Previous training in psychology focused primarily on qualitative interpretation, conceptual modelling, and theoretical critique, whereas this module required engagement with computational data systems, structured datasets, and technical workflows. This created an early sense of cognitive displacement, as the dominant learning environment moved away from narrative analysis toward procedural and quantitative reasoning (Kolb, 1984).

The structure of the module made it clear that effective data wrangling depends on a sequential pipeline of activities: data sourcing, extraction, cleaning, staging, modelling, and validation (Kazil and Jarmul, 2016). At the outset, these stages were difficult to distinguish, and progress felt slow as fundamental workflows—particularly scripting for parsing and cleansing—had to be repeatedly reviewed. This period highlighted a shift in learning style; understanding did not emerge through theoretical synthesis alone but required repetitive practice and failure-testing. Educational research identifies this process as experiential learning, where skill acquisition occurs through iterative trial, reflection, and refinement rather than immediate comprehension (Kolb, 1984).

As competence increased, conceptual connections became clearer. Data cleaning and normalisation were revealed not solely as technical exercises but as safeguards protecting interpretive validity — a principle directly aligning with research ethics in psychology where data reliability underpins evidence-based judgement (Babbie, 2020). Work on the UNICEF dataset (Units 4 and 5) demonstrated the importance of recognising missing values, inconsistencies, and classification ambiguities before any inferential analysis can begin. Without these steps, statistical conclusions risk distortion from structurally flawed data inputs (Kazil and Jarmul, 2016).

The group project reinforced these lessons further. Contributions focused on mapping the transition from raw billing data to normalised relational tables. Applying 3NF to student assessment data and electricity billing datasets exposed how unmanaged redundancy creates update and deletion anomalies, directly threatening transactional correctness (Harrington, 2016). Initial attempts at explanation remained somewhat abstract; tutor feedback later highlighted that system rationale must be rooted in the practical operating environment rather than general comparisons between database types.

This observation became more apparent during the Unit 11 implementation phase. Deploying the SQLite database transformed theoretical discussions of transaction safety into functional system requirements. The necessity of ACID compliance—atomicity, consistency, isolation, and durability—became operationally meaningful when testing primary-foreign key relationships, failed deletes, and multi-table joins (Connolly and Begg, 2015). What previously appeared as textbook definitions evolved into mechanisms directly protecting financial record integrity and regulatory accountability. Running integrity checks after transactional insertions clarified that correct design cannot rest on schema modelling alone; database enforcement and rollback mechanisms are equally essential (Gray and Reuter, 1993).

Emotionally, adaptation followed a gradual trajectory. Early discomfort stemmed from perceived slowness relative to prior academic pursuits. However, recognising that unfamiliar technical learning requires extended consolidation reshaped expectations of competence development (Illeris, 2018). The module demanded resilience rather than immediate fluency, promoting a more sustainable learning mindset. Instead of retreating from areas of difficulty, engagement shifted toward persistence and incremental mastery.

External circumstances, including intermittent access to stable study environments, further compounded challenges. Support received from members of the local community, including provision of workspace and internet connectivity, introduced new reflections on educational privilege and collective investment in personal development. Social learning theory emphasises that peer and community contexts influence both motivation and persistence (Bandura, 1997). This experience underscored the role of shared belief in individual potential as a driver of academic continuity.

Collectively, the skills developed extend beyond technical programming. Practical competencies include structured data extraction, automated cleaning scripts, normalisation modelling, SQL execution, and transaction testing. More critically, broader professional skills emerged through collaboration: procedural communication, accountability division in team work, and constructive integration of academic feedback. These capacities mirror organisational analytics roles where collaboration between analysts, developers, and compliance stakeholders is central to system effectiveness (Provost and Fawcett, 2013).

Looking forward, this learning will directly inform future research practice. Data collection protocols, metadata management, and reproducibility principles now form part of standard methodological awareness rather than isolated technical challenges. By applying robust wrangling pipelines to psychological research designs, longitudinal data management and mixed-method integrations may be conducted with significantly higher reliability.

In conclusion, the module represents a turning point from subject comfort toward skill expansion. Mastery was not immediate, yet the discipline required to persevere through complexity produced transferable professional confidence. Competence is now viewed not as a starting condition but as an outcome built through sustained effort. This adaptive learning orientation is likely to remain a defining feature of continued academic and professional development.

---

### References — Reflection

Babbie, E. (2020) *The Practice of Social Research*. 15th edn. Cengage.

Bandura, A. (1997) *Self-Efficacy: The Exercise of Control*. New York: Freeman.

Connolly, T. and Begg, C. (2015) *Database Systems*. Pearson.

Gray, J. and Reuter, A. (1993) *Transaction Processing*. Morgan Kaufmann.

Harrington, J.L. (2016) *Relational Database Design*. Morgan Kaufmann.

Illeris, K. (2018) *Contemporary Theories of Learning*. Routledge.

Kazil, J. and Jarmul, K. (2016) *Data Wrangling with Python*. O’Reilly.

Kolb, D. (1984) *Experiential Learning*. Prentice-Hall.

Provost, F. and Fawcett, T. (2013) *Data Science for Business*. O’Reilly.

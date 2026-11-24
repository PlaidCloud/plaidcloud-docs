---
title: Modeling Learning Path
description: What to read before the PlaidCloud Modeling Practitioner and Expert labs, and what each lab asks you to do.
sidebar:
  label: Modeling
---

The Modeling track is about dimensions and allocations: building hierarchies, spreading costs by drivers, and proving the results tie out. Start with the [Foundations](/guides/certification/foundations/) path. For how labs work, see [PlaidCloud Certification](/guides/certification/).

## Practitioner

### Read in This Order

1. [Getting Started with Dimensions](/guides/dimensions/getting-started/)
2. [Managing Hierarchies](/guides/projects/managing-hierarchies/)
3. [Design a Dimension Hierarchy](/get-started/tutorials/design-a-dimension/)
4. [Allocations Quick Start](/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split](/reference/workflow-steps/allocation/allocation-split/)
6. [Build an Allocation Model](/get-started/tutorials/build-an-allocation/)
7. [Allocation Results](/guides/allocations/results/allocation-results/)
8. [Viewing Workflow Log](/guides/workflows/viewing-workflow-log/)

### What the Lab Asks

The lab is called *Modeling: allocate shared IT cost*.

A table lists each department and its parent. You build a dimension whose main hierarchy is exactly that tree. Then, in the lab's workflow, you allocate a cost pool to the departments in proportion to their headcount, with one result row per department. A second driver table is there too, and it isn't the driver for this pool.

The lab checks that the workflow runs, that the hierarchy is right, that the allocated total ties to the source, and that each department gets the right amount.

## Expert

The Expert lab is timed: you have 4 hours from the moment you start it.

### Read in This Order

1. [Configure an Allocation](/guides/allocations/setup/configure-an-allocation/)
2. [Troubleshooting Allocations](/guides/allocations/results/troubleshooting-allocations/)
3. [Tracing Allocations with an MCP-Connected AI Agent](/integrations/ai-coding-agents/tracing-allocations/)
4. [Allocation Results](/guides/allocations/results/allocation-results/)
5. [Try a Driver What-If](/guides/allocations/results/driver-what-if/)
6. [Managing Hierarchies](/guides/projects/managing-hierarchies/)

### What the Lab Asks

The lab is called *Modeling Expert: repair the allocation model*.

A two-stage allocation model no longer ties to the ledger, and some departments are clearly wrong. You trace the cause and fix the model: each stage allocates exactly its pool, the department totals are right and add up to the ledger, and the department dimension holds only the departments that exist. No balancing row may be used to make anything tie. Then you add a step that shows what IT would cost each department if it were allocated by floor space instead of headcount.

The lab checks that the workflow runs, that the hierarchy is right, that each stage and the department totals tie to the ledger, that each department gets the right total, and that the floor space scenario is right.

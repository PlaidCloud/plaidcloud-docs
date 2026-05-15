---
title: Why are Allocations Useful
description: Understand why cost allocations are useful in PlaidCloud for activity-based costing, chargeback, and profitability analysis.
sidebar:
  order: 2
---

Allocations spread a pool of values (typically cost, but it works for any aggregate) across consumers based on a measurable driver. They answer the question: *if we incur this cost, how should it be assigned to the things that consume it?*

## Common use cases

### Activity-based costing

You know your total marketing spend for a quarter. You want to attribute it to specific products based on something measurable — campaign hours, leads generated, qualified opportunities. An allocation spreads the marketing pool across products using your chosen driver, giving each product a fully-loaded cost.

### IT chargeback

You spend $X running shared infrastructure (compute, storage, licensing). Each business unit consumes a different amount. An allocation spreads the IT cost across units based on usage metrics — VM hours, storage GB, license seats — so each unit's P&L reflects what it actually consumed.

### Shared service distribution

Finance, HR, legal, facilities — central functions that serve the whole company. Allocations distribute their cost across the divisions they serve, typically by headcount, revenue, or a weighted blend.

### Transfer pricing

For multi-entity organizations, allocations model how internal services are priced between entities. The output drives intercompany journal entries.

### Profitability analysis

You have revenue at the product or customer level. You have costs at various pools (sales, support, infrastructure, COGS). Allocations bring everything together at the product/customer grain so you can see actual margin.

### Bill of materials costing

Cost flows down a hierarchy of components. Each step in the BoM is an allocation: subassembly costs spread to assemblies, assemblies to finished goods, finished goods to SKUs.

## What allocations save you from

Without an allocation engine, you'd build these models in spreadsheets — fragile, hard to audit, hard to repeat with updated data. PlaidCloud allocations give you:

- **Reproducible models** that re-run automatically as source data refreshes
- **Audit trail** showing which source rows contributed to which target rows
- **Layered allocations** where outputs feed further allocations
- **Dimensional integration** so allocations respect your existing hierarchies

## Next steps

- [Allocations Quick Start](/guides/allocations/getting-started/allocations-quick-start/) — build one in 30 minutes
- [Rule-Based Tagging](/guides/allocations/getting-started/rule-based-tagging/) — control allocation behavior by row
- [Configure an allocation](/guides/allocations/setup/configure-an-allocation/) — full configuration reference

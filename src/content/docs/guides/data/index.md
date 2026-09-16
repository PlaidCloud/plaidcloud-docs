---
title: Data Management - Tabular
description: Manage tabular data in PlaidCloud using tables, views, and the high-performance Lakehouse engine for any-scale data processing.
sidebar:
  label: Data Management - Tabular
---

PlaidCloud's data layer is built around **tables** (structured row-and-column data) and **views** (saved queries over tables). Both live inside a project and are powered by the Lakehouse engine, which scales from small reference tables to billion-row analytical datasets without configuration changes.

## What's in This Section

- [Tables and views](/guides/data/tables-views/) — what each is, when to use which, and how they interact
- [Table explorer](/guides/data/table-explorer/) — browse and inspect tables in your project
- [Currency data type](/guides/data/currency-data-type/) — an exact, half-width column type for money values, and when to choose it over Numeric
- [Table snapshots](/guides/data/table-snapshots/) — browse snapshot history, view data as of a past snapshot, and revert or restore a table
- [Publishing data](/guides/data/publish/) — make project tables available to dashboards, BI tools, and downstream systems, and review their performance guidance
- [Selecting the latest record in a large history table](/guides/data/selecting-latest-record-in-large-history-table/) — a common pattern with a performance-aware solution
- [Geocoding API](/guides/data/geocoding-api/) — migrate a Google or Mapbox geocoding integration to PlaidCloud's REST geocoding endpoints
- [Drive-Time Routing API](/guides/data/drive-time-routing-api/) — opt-in preview: drive-time isochrones and nearest-by-drive-time ranking over REST

## Where Data Comes From

Tables are typically populated by **workflows** — automated pipelines that import data, transform it, and write results back. See [Workflows](/guides/workflows/) for how to build them, and [Workflow step reference](/reference/workflow-steps/) for every step type you can use.

For connecting external systems as data sources, see [Connections (guide)](/guides/connections/) and [Connectors (reference)](/reference/connectors/).

## Related

- [Concepts](/get-started/concepts/) — how tables relate to workflows, dimensions, and the broader data model
- [Projects](/guides/projects/) — projects own the tables; tables don't exist outside a project
- [Dashboards](/guides/dashboards/) — consume published tables for visualization

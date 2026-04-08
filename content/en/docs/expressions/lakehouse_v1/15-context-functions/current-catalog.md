---
title: CURRENT_CATALOG
description: "Learn how to use the CURRENT_CATALOG context function in PlaidCloud Lakehouse. Returns the name of the catalog currently in use for the session."
---

Returns the name of the catalog currently in use for the session.

## SQL Syntax

```sql
CURRENT_CATALOG()
```

## SQL Examples

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
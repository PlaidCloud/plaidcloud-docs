---
title: TRY_CAST
---

Converts a value from one data type to another. Returns NULL on error.

See also: [CAST](cast)

## SQL Syntax

```sql
TRY_CAST( <expr> AS <data_type> )
```

## SQL Examples

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
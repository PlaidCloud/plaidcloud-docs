---
title: IS_NOT_NULL
---

Checks whether a value is not NULL.

## SQL Syntax

```sql
IS_NOT_NULL(<expr>)
```

## SQL Examples

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
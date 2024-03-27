---
title: DATABASE
---

Returns the name of the currently selected database. If no database is selected, then this function returns `default`.

## SQL Syntax

```sql
DATABASE()
```

## SQL Examples

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
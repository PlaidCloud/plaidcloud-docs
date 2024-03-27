---
title: "[ NOT ] IN"
---

Checks whether a value is (or is not) in an explicit list.

## SQL Syntax

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## SQL Examples

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```
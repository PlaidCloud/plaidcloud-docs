---
title: IFNULL
---

If `<expr1>` is NULL, returns `<expr2>`, otherwise returns `<expr1>`.

## SQL Syntax

```sql
IFNULL(<expr1>, <expr2>)
```

## Aliases

- [NVL](nvl.md)

## SQL Examples

```sql
SELECT IFNULL(NULL, 'b'), IFNULL('a', 'b');

┌──────────────────────────────────────┐
│ ifnull(null, 'b') │ ifnull('a', 'b') │
├───────────────────┼──────────────────┤
│ b                 │ a                │
└──────────────────────────────────────┘

SELECT IFNULL(NULL, 2), IFNULL(1, 2);

┌────────────────────────────────┐
│ ifnull(null, 2) │ ifnull(1, 2) │
├─────────────────┼──────────────┤
│               2 │            1 │
└────────────────────────────────┘
```
---
title: GET
---

Returns an element from an array by index (1-based).

## SQL Syntax

```sql
GET( <array>, <index> )
```

## Aliases

- [ARRAY_GET](array-get.md)

## SQL Examples

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
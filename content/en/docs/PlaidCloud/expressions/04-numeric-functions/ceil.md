---
title: CEIL
---

Rounds the number up.

## SQL Syntax

```sql
CEIL( <x> )
```

## Aliases

- [CEILING](ceiling.md)

## SQL Examples

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```
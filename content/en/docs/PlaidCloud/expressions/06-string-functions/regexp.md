---
title: REGEXP
---

Returns `true` if the string `<expr>` matches the regular expression specified by the `<pattern>`, `false` otherwise.

## SQL Syntax

```sql
<expr> REGEXP <pattern>
```

## Aliases

- [RLIKE](rlike.md)

## SQL Examples

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```
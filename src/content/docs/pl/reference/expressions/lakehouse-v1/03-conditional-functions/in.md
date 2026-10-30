---
title: "[ NOT ] IN (Lakehouse v1)"
description: "[ NOT ] IN — prawda, jeśli wartość jest równa (lub nie jest równa) dowolnemu elementowi jawnej listy."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/in.md
---

Sprawdza, czy wartość znajduje się (lub nie znajduje się) na jawnej liście.

## Składnia Analyze

```python
table.columns.in_((<value1>, <value2> ...))
```

## Przykłady Analyze

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## Składnia SQL

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## Przykłady SQL

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```

---
title: "[ NOT ] IN (Lakehouse v1)"
description: "[ NOT ] IN — verdadero si un valor es igual (o distinto) a cualquier elemento de una lista explícita."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/in.md
---

Comprueba si un valor está (o no está) en una lista explícita.

## Sintaxis de Analyze

```python
table.columns.in_((<value1>, <value2> ...))
```

## Ejemplos de Analyze

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## Sintaxis de SQL

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## Ejemplos de SQL

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```

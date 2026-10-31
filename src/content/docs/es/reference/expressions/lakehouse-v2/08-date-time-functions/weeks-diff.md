---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF — devuelve el número de semanas entre dos fechas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-diff.md
---

Devuelve el número de semanas entre dos fechas.

## Sintaxis de Analyze

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Ejemplos de Analyze

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## Sintaxis de SQL

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## Ejemplos de SQL

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```

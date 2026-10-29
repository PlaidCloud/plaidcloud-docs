---
title: DATE_DIFF (Lakehouse v2)
description: DATE_DIFF — devuelve la diferencia entre dos fechas en la unidad especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-diff.md
---

Devuelve la diferencia entre dos fechas en la unidad especificada.

## Sintaxis de Analyze

```python
func.date_diff(<unit>, <start>, <end>)
```

## Ejemplos de Analyze

```python
func.date_diff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## Sintaxis de SQL

```sql
DATE_DIFF(<unit>, <start>, <end>)
```

## Ejemplos de SQL

```sql
SELECT DATE_DIFF('DAY', '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```

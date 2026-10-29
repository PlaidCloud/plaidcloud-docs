---
title: DATEDIFF (Lakehouse v2)
description: DATEDIFF — devuelve el número de días entre dos fechas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/datediff.md
---

Devuelve el número de días entre dos fechas.

## Sintaxis de Analyze

```python
func.datediff(<end_date>, <start_date>)
```

## Ejemplos de Analyze

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## Sintaxis de SQL

```sql
DATEDIFF(<end_date>, <start_date>)
```

## Ejemplos de SQL

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```

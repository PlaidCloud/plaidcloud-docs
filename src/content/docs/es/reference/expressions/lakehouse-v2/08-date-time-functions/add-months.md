---
title: ADD_MONTHS (Lakehouse v2)
description: ADD_MONTHS — suma un número específico de meses a una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/add-months.md
---

Suma un número específico de meses a una fecha.

## Sintaxis de Analyze

```python
func.add_months(<date>, <months>)
```

## Ejemplos de Analyze

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
ADD_MONTHS(<date>, <months>)
```

## Ejemplos de SQL

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```

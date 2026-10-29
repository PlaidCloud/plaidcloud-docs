---
title: DAYS_ADD (Lakehouse v2)
description: DAYS_ADD — suma un número específico de días a una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-add.md
---

Suma un número específico de días a una fecha.

## Sintaxis de Analyze

```python
func.days_add(<date>, <n>)
```

## Ejemplos de Analyze

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
DAYS_ADD(<date>, <n>)
```

## Ejemplos de SQL

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```

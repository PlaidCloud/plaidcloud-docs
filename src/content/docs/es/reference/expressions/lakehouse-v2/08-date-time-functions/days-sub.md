---
title: DAYS_SUB (Lakehouse v2)
description: DAYS_SUB — resta un número específico de días a una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-sub.md
---

Resta un número específico de días a una fecha.

## Sintaxis de Analyze

```python
func.days_sub(<date>, <n>)
```

## Ejemplos de Analyze

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
DAYS_SUB(<date>, <n>)
```

## Ejemplos de SQL

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```

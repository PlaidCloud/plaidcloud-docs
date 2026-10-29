---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB — resta un número específico de años de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-sub.md
---

Resta un número específico de años de una fecha.

## Sintaxis de Analyze

```python
func.years_sub(<date>, <n>)
```

## Ejemplos de Analyze

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
YEARS_SUB(<date>, <n>)
```

## Ejemplos de SQL

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```

---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB — resta un número específico de meses de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-sub.md
---

Resta un número específico de meses de una fecha.

## Sintaxis de Analyze

```python
func.months_sub(<date>, <n>)
```

## Ejemplos de Analyze

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
MONTHS_SUB(<date>, <n>)
```

## Ejemplos de SQL

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```

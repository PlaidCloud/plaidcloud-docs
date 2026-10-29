---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB — resta un número específico de semanas de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-sub.md
---

Resta un número específico de semanas de una fecha.

## Sintaxis de Analyze

```python
func.weeks_sub(<date>, <n>)
```

## Ejemplos de Analyze

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
WEEKS_SUB(<date>, <n>)
```

## Ejemplos de SQL

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```

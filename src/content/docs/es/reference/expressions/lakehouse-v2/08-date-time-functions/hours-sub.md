---
title: HOURS_SUB (Lakehouse v2)
description: HOURS_SUB — resta un número específico de horas a un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-sub.md
---

Resta un número específico de horas a un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.hours_sub(<datetime>, <n>)
```

## Ejemplos de Analyze

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
HOURS_SUB(<datetime>, <n>)
```

## Ejemplos de SQL

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```

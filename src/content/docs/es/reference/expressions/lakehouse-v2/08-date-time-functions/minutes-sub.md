---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB — resta un número específico de minutos de un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

Resta un número específico de minutos de un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.minutes_sub(<datetime>, <n>)
```

## Ejemplos de Analyze

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
MINUTES_SUB(<datetime>, <n>)
```

## Ejemplos de SQL

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```

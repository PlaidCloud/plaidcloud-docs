---
title: SECONDS_SUB (Lakehouse v2)
description: SECONDS_SUB — resta un número específico de segundos de un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-sub.md
---

Resta un número específico de segundos de un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.seconds_sub(<datetime>, <n>)
```

## Ejemplos de Analyze

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
SECONDS_SUB(<datetime>, <n>)
```

## Ejemplos de SQL

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```

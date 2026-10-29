---
title: MICROSECONDS_SUB (Lakehouse v2)
description: MICROSECONDS_SUB — resta un número específico de microsegundos de un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-sub.md
---

Resta un número específico de microsegundos de un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.microseconds_sub(<datetime>, <n>)
```

## Ejemplos de Analyze

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## Ejemplos de SQL

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```

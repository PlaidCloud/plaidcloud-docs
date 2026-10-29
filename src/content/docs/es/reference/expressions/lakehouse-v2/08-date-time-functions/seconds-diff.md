---
title: SECONDS_DIFF (Lakehouse v2)
description: SECONDS_DIFF — devuelve el número de segundos entre dos valores de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-diff.md
---

Devuelve el número de segundos entre dos valores de fecha y hora.

## Sintaxis de Analyze

```python
func.seconds_diff(<end>, <start>)
```

## Ejemplos de Analyze

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## Sintaxis de SQL

```sql
SECONDS_DIFF(<end>, <start>)
```

## Ejemplos de SQL

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```

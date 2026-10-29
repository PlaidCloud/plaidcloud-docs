---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF — devuelve el número de minutos entre dos valores de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-diff.md
---

Devuelve el número de minutos entre dos valores de fecha y hora.

## Sintaxis de Analyze

```python
func.minutes_diff(<end>, <start>)
```

## Ejemplos de Analyze

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## Sintaxis de SQL

```sql
MINUTES_DIFF(<end>, <start>)
```

## Ejemplos de SQL

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```

---
title: HOURS_DIFF (Lakehouse v2)
description: HOURS_DIFF — devuelve el número de horas entre dos valores de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-diff.md
---

Devuelve el número de horas entre dos valores de fecha y hora.

## Sintaxis de Analyze

```python
func.hours_diff(<end>, <start>)
```

## Ejemplos de Analyze

```python
func.hours_diff('2024-01-02 10:00:00', '2024-01-01 10:00:00')

┌────┐
│ 24  │
└────┘
```

## Sintaxis de SQL

```sql
HOURS_DIFF(<end>, <start>)
```

## Ejemplos de SQL

```sql
SELECT HOURS_DIFF('2024-01-02 10:00:00', '2024-01-01 10:00:00');

┌────┐
│ 24  │
└────┘
```

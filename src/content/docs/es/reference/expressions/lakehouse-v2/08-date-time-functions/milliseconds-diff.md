---
title: MILLISECONDS_DIFF (Lakehouse v2)
description: MILLISECONDS_DIFF — devuelve el número de milisegundos entre dos valores de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/milliseconds-diff.md
---

Devuelve el número de milisegundos entre dos valores de fecha y hora.

## Sintaxis de Analyze

```python
func.milliseconds_diff(<end>, <start>)
```

## Ejemplos de Analyze

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## Sintaxis de SQL

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## Ejemplos de SQL

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```

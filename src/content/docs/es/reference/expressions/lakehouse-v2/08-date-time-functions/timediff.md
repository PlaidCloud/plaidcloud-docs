---
title: TIMEDIFF (Lakehouse v2)
description: TIMEDIFF — devuelve la diferencia entre dos valores de hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timediff.md
---

Devuelve la diferencia entre dos valores de hora.

## Sintaxis de Analyze

```python
func.timediff(<time1>, <time2>)
```

## Ejemplos de Analyze

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## Sintaxis de SQL

```sql
TIMEDIFF(<time1>, <time2>)
```

## Ejemplos de SQL

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```

---
title: TIMEDIFF (Lakehouse v2)
description: TIMEDIFF — devolve a diferença entre dois valores de hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timediff.md
---

Devolve a diferença entre dois valores de hora.

## Sintaxe de Analyze

```python
func.timediff(<time1>, <time2>)
```

## Exemplos de Analyze

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## Sintaxe SQL

```sql
TIMEDIFF(<time1>, <time2>)
```

## Exemplos SQL

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```

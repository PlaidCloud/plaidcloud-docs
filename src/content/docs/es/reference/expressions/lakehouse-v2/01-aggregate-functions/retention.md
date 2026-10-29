---
title: RETENTION (Lakehouse v2)
description: RETENTION — calcula la retención para un conjunto de eventos. Devuelve una matriz de 0 y 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/retention.md
---

Calcula la retención para un conjunto de eventos. Devuelve una matriz de 0 y 1.

## Sintaxis de Analyze

```python
func.retention(cond1, cond2)
```

## Ejemplos de Analyze

```python
func.retention(get_column(table, 'day1'), get_column(table, 'day2'))
```

## Sintaxis de SQL

```sql
RETENTION(cond1, cond2)
```

## Ejemplos de SQL

```sql
SELECT uid, RETENTION(dt='2024-01-01', dt='2024-01-02', dt='2024-01-03')
FROM events GROUP BY uid;

┌─────┬────────────┐
│ uid │ retention  │
├─────┼────────────┤
│   1 │ [1,1,0]    │
│   2 │ [1,0,0]    │
│   3 │ [1,1,1]    │
└─────┴────────────┘
```

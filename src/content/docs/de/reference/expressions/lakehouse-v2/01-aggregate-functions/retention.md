---
title: RETENTION (Lakehouse v2)
description: RETENTION – berechnet die Retention für eine Menge von Ereignissen. Gibt ein Array aus 0 und 1 zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/retention.md
---

Berechnet die Retention für eine Menge von Ereignissen. Gibt ein Array aus 0 und 1 zurück.

## Analyze-Syntax

```python
func.retention(cond1, cond2)
```

## Analyze-Beispiele

```python
func.retention(get_column(table, 'day1'), get_column(table, 'day2'))
```

## SQL-Syntax

```sql
RETENTION(cond1, cond2)
```

## SQL-Beispiele

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

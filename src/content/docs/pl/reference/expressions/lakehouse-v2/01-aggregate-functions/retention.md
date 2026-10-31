---
title: RETENTION (Lakehouse v2)
description: RETENTION — oblicza retencję dla zbioru zdarzeń. Zwraca tablicę zer i jedynek.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/retention.md
---

Oblicza retencję dla zbioru zdarzeń. Zwraca tablicę zer i jedynek.

## Składnia Analyze

```python
func.retention(cond1, cond2)
```

## Przykłady Analyze

```python
func.retention(get_column(table, 'day1'), get_column(table, 'day2'))
```

## Składnia SQL

```sql
RETENTION(cond1, cond2)
```

## Przykłady SQL

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

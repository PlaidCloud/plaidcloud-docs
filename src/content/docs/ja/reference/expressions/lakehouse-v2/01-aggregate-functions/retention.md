---
title: RETENTION (Lakehouse v2)
description: RETENTION — イベントの集合に対するリテンションを計算します。0 と 1 の配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/retention.md
---

イベントの集合に対するリテンションを計算します。0 と 1 の配列を返します。

## Analyzeの構文

```python
func.retention(cond1, cond2)
```

## Analyzeの例

```python
func.retention(get_column(table, 'day1'), get_column(table, 'day2'))
```

## SQLの構文

```sql
RETENTION(cond1, cond2)
```

## SQLの例

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

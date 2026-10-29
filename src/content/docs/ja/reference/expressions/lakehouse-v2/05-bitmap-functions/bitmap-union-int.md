---
title: BITMAP_UNION_INT (Lakehouse v2)
description: BITMAP_UNION_INT — 重複を除いた整数値の数を返します（集計）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-int.md
---

重複を除いた整数値の数を返します（集計）。

## Analyzeの構文

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Analyzeの例

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## SQLの構文

```sql
BITMAP_UNION_INT(<id>)
```

## SQLの例

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```

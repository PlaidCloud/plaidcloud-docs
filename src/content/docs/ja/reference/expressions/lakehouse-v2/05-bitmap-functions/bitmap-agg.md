---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG — 整数値をビットマップに集約します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-agg.md
---

整数値をビットマップに集約します。

## Analyzeの構文

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyzeの例

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_AGG(<id>)
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```

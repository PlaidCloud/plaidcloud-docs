---
title: BITMAP（Lakehouse v2）
description: BITMAP — 値の集合のビットマップ和集合を返します。通常はBITMAP_AGGと組み合わせて使用します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bitmap.md
---

値の集合のビットマップ和集合を返します。通常はBITMAP_AGGと組み合わせて使用します。

## Analyzeの構文

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyzeの例

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP(<id>)
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```

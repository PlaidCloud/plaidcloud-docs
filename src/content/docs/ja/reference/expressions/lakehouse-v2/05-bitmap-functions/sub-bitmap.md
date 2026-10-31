---
title: SUB_BITMAP (Lakehouse v2)
description: SUB_BITMAP — 指定した位置から始まり、要素数の上限を指定したサブビットマップを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/sub-bitmap.md
---

指定した位置から始まり、要素数の上限を指定したサブビットマップを返します。

## Analyzeの構文

```python
func.sub_bitmap(<bitmap>, <offset>, <limit>)
```

## Analyzeの例

```python
func.sub_bitmap(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
SUB_BITMAP(<bitmap>, <offset>, <limit>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(SUB_BITMAP(BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```

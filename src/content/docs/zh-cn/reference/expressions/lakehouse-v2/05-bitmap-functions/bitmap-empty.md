---
title: BITMAP_EMPTY (Lakehouse v2)
description: BITMAP_EMPTY：返回空位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-empty.md
---

返回空位图。

## Analyze 语法

```python
func.bitmap_empty()
```

## Analyze 示例

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## SQL 语法

```sql
BITMAP_EMPTY()
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```

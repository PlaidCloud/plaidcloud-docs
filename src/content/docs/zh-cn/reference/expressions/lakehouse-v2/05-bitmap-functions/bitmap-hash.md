---
title: BITMAP_HASH (Lakehouse v2)
description: BITMAP_HASH：计算值的 32 位哈希，并返回包含该哈希的位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash.md
---

计算值的 32 位哈希，并返回包含该哈希的位图。

## Analyze 语法

```python
func.bitmap_hash(<value>)
```

## Analyze 示例

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_HASH(<value>)
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```

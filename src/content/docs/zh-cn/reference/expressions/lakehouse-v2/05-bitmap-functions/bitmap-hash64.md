---
title: BITMAP_HASH64 (Lakehouse v2)
description: BITMAP_HASH64：计算值的 64 位哈希，并返回包含该哈希的位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash64.md
---

计算值的 64 位哈希，并返回包含该哈希的位图。

## Analyze 语法

```python
func.bitmap_hash64(<value>)
```

## Analyze 示例

```python
func.bitmap_hash64('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_HASH64(<value>)
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_HASH64('hello'));

┌───┐
│ 1 │
└───┘
```

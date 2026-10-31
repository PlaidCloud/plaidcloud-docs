---
title: BITMAP_HAS_ANY (Lakehouse v2)
description: BITMAP_HAS_ANY：检查两个位图是否有共同元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-has-any.md
---

检查两个位图是否有共同元素。

## Analyze 语法

```python
func.bitmap_has_any(<bm1>, <bm2>)
```

## Analyze 示例

```python
func.bitmap_has_any(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
BITMAP_HAS_ANY(<bm1>, <bm2>)
```

## SQL 示例

```sql
SELECT BITMAP_HAS_ANY(BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3'));

┌───┐
│ 1 │
└───┘
```

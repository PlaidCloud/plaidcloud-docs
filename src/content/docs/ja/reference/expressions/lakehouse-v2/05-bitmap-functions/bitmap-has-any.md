---
title: BITMAP_HAS_ANY (Lakehouse v2)
description: BITMAP_HAS_ANY — 2 つのビットマップに共通の要素があるかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-has-any.md
---

2 つのビットマップに共通の要素があるかどうかを確認します。

## Analyzeの構文

```python
func.bitmap_has_any(<bm1>, <bm2>)
```

## Analyzeの例

```python
func.bitmap_has_any(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
BITMAP_HAS_ANY(<bm1>, <bm2>)
```

## SQLの例

```sql
SELECT BITMAP_HAS_ANY(BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3'));

┌───┐
│ 1 │
└───┘
```

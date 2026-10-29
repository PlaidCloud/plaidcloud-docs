---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ — 配列が別の配列のすべての要素を同じ順序で含んでいるかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

配列が別の配列のすべての要素を同じ順序で含んでいるかどうかを確認します。

## Analyzeの構文

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Analyzeの例

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## SQLの例

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```

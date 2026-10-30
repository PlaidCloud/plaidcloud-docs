---
title: ARRAY_CONTAINS_ALL (Lakehouse v2)
description: ARRAY_CONTAINS_ALL — 配列が別の配列のすべての要素を含んでいるかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-all.md
---

配列が別の配列のすべての要素を含んでいるかどうかを確認します。

## Analyzeの構文

```python
func.array_contains_all([1,2,3], [1,2])
```

## Analyzeの例

```python
func.array_contains_all([1, 2, 3], [1, 2])

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
ARRAY_CONTAINS_ALL([1,2,3], [1,2])
```

## SQLの例

```sql
SELECT ARRAY_CONTAINS_ALL([1, 2, 3], [1, 2]);

┌───┐
│ 1 │
└───┘
```

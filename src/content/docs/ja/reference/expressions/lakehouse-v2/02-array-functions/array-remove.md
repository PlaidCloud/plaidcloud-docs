---
title: ARRAY_REMOVE (Lakehouse v2)
description: ARRAY_REMOVE — 指定した要素と一致するすべての要素を配列から削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-remove.md
---

指定した要素と一致するすべての要素を配列から削除します。

## Analyzeの構文

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Analyzeの例

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## SQLの構文

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## SQLの例

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```

---
title: ARRAY_DISTINCT (Lakehouse v2)
description: ARRAY_DISTINCT — 配列から重複する要素を削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-distinct.md
---

配列から重複する要素を削除します。

## Analyzeの構文

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Analyzeの例

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## SQLの構文

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## SQLの例

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```

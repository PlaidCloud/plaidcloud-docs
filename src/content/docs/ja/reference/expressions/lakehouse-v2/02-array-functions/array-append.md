---
title: ARRAY_APPEND (Lakehouse v2)
description: ARRAY_APPEND — 配列の末尾に要素を追加します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-append.md
---

配列の末尾に要素を追加します。

## Analyzeの構文

```python
func.array_append([1, 2, 3], 4)
```

## Analyzeの例

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQLの構文

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## SQLの例

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

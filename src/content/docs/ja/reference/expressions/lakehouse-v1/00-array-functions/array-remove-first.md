---
title: ARRAY_REMOVE_FIRST (Lakehouse v1)
description: ARRAY_REMOVE_FIRST — 配列から最初の要素を削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-first.md
---

配列から最初の要素を削除します。

## Analyzeの構文

```python
func.array_remove_first( <array> )
```

## Analyzeの例

```python
func.array_remove_first([1, 2, 3]) 

┌─────────────────────────────────────┐
│ func.array_remove_first([1, 2, 3])  │
├─────────────────────────────────────┤
│ [2,3]                               │
└─────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_REMOVE_FIRST( <array> )
```

## SQLの例

```sql
SELECT ARRAY_REMOVE_FIRST([1, 2, 3]);

┌───────────────────────────────┐
│ array_remove_first([1, 2, 3]) │
├───────────────────────────────┤
│ [2,3]                         │
└───────────────────────────────┘
```

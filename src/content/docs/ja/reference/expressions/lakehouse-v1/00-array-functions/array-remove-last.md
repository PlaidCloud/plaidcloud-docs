---
title: ARRAY_REMOVE_LAST (Lakehouse v1)
description: ARRAY_REMOVE_LAST — 配列から最後の要素を削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-last.md
---

配列から最後の要素を削除します。

## Analyzeの構文

```python
func.array_remove_last( <array> )
```

## Analyzeの例

```python
func.array_remove_last([1, 2, 3]) 

┌────────────────────────────────────┐
│ func.array_remove_last([1, 2, 3])  │
├────────────────────────────────────┤
│ [1,2]                              │
└────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_REMOVE_LAST( <array> )
```

## SQLの例

```sql
SELECT ARRAY_REMOVE_LAST([1, 2, 3]);

┌──────────────────────────────┐
│ array_remove_last([1, 2, 3]) │
├──────────────────────────────┤
│ [1,2]                        │
└──────────────────────────────┘
```

---
title: ARRAY_DISTINCT (Lakehouse v1)
description: ARRAY_DISTINCT — 元の順序を保持せずに、配列からすべての重複とNULLを削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-distinct.md
---

元の順序を保持せずに、配列からすべての重複とNULLを削除します。

## Analyzeの構文

```python
func.array_distinct( <array> )
```

## Analyzeの例

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_DISTINCT( <array> )
```

## SQLの例

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```

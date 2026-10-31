---
title: ARRAY_FLATTEN (Lakehouse v1)
description: ARRAY_FLATTEN — ネストされた配列を平坦化し、1階層の配列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-flatten.md
---

ネストされた配列を平坦化し、1階層の配列に変換します。

## Analyzeの構文

```python
func.array_flatten( <array> )
```

## Analyzeの例

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_FLATTEN( <array> )
```

## SQLの例

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```

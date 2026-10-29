---
title: ARRAY_INDEXOF (Lakehouse v1)
description: ARRAY_INDEXOF — 配列に要素が含まれている場合、その要素のインデックス（1から始まる）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-indexof.md
---

配列に要素が含まれている場合、その要素のインデックス（1から始まる）を返します。

## Analyzeの構文

```python
func.array_indexof( <array>, <element> )
```

## Analyzeの例

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## SQLの例

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```

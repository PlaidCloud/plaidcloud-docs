---
title: ARRAY_REDUCE (Lakehouse v1)
description: ARRAY_REDUCE — 配列の要素にラムダ関数を繰り返し適用し、配列を1つの値にまとめます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-reduce.md
---

配列の要素にラムダ関数を繰り返し適用し、配列を1つの値にまとめます。

## Analyzeの構文

```python
func.array_reduce( <array>, <lambda> )
```

## Analyzeの例

```python
func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))

┌─────────────────────────────────────────────────────┐
│ func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))  │
├─────────────────────────────────────────────────────┤
│                                                  10 │
└─────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_REDUCE( <array>, <lambda> )
```

## SQLの例

```sql
SELECT ARRAY_REDUCE([1, 2, 3, 4], (x,y) -> x + y);

┌───────────────────────────────────────────────┐
│ array_reduce([1, 2, 3, 4], (x, y) -> (x + y)) │
├───────────────────────────────────────────────┤
│                                            10 │
└───────────────────────────────────────────────┘
```

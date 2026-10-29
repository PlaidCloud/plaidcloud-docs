---
title: ARRAY_FILTER (Lakehouse v1)
description: ARRAY_FILTER — ラムダ関数がtrueを返す入力配列の要素から、新しい配列を作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-filter.md
---

ラムダ関数がtrueを返す入力配列の要素から、新しい配列を作成します。

## Analyzeの構文

```python
func.array_filter( <array>, <lambda> )
```

## Analyzeの例

```python
func.array_filter([1, 2, 3], x -> (x > 1))

┌─────────────────────────────────────────────┐
│ func.array_filter([1, 2, 3], x -> (x > 1))  │
├─────────────────────────────────────────────┤
│ [2,3]                                       │
└─────────────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_FILTER( <array>, <lambda> )
```

## SQLの例

```sql
SELECT ARRAY_FILTER([1, 2, 3], x -> x > 1);

┌───────────────────────────────────────┐
│ array_filter([1, 2, 3], x -> (x > 1)) │
├───────────────────────────────────────┤
│ [2,3]                                 │
└───────────────────────────────────────┘
```

---
title: ARRAY_FILTER (Lakehouse v2)
description: ARRAY_FILTER — ラムダ式を使用して配列の要素をフィルターします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-filter.md
---

ラムダ式を使用して配列の要素をフィルターします。

## Analyzeの構文

```python
func.array_filter(get_column(table, 'arr'), lambda x: x > 2)
```

## Analyzeの例

```python
func.array_filter([1, 2, 3, 4, 5], lambda x: x > 2)

┌─────────┐
│ [3,4,5] │
└─────────┘
```

## SQLの構文

```sql
ARRAY_FILTER(<arr>, lambda x: x > 2)
```

## SQLの例

```sql
SELECT ARRAY_FILTER([1, 2, 3, 4, 5], x -> x > 2);

┌─────────┐
│ [3,4,5] │
└─────────┘
```

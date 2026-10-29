---
title: ARRAY_MAP (Lakehouse v2)
description: ARRAY_MAP — 配列の各要素にラムダ式を適用します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-map.md
---

配列の各要素にラムダ式を適用します。

## Analyzeの構文

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Analyzeの例

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## SQLの構文

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## SQLの例

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```

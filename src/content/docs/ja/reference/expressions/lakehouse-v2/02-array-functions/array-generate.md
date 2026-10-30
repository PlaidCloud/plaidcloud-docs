---
title: ARRAY_GENERATE (Lakehouse v2)
description: ARRAY_GENERATE — 連続した値の配列を生成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-generate.md
---

連続した値の配列を生成します。

## Analyzeの構文

```python
func.array_generate(1, 5)
```

## Analyzeの例

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## SQLの構文

```sql
ARRAY_GENERATE(1, 5)
```

## SQLの例

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

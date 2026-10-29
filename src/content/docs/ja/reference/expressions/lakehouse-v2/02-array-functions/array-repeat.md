---
title: ARRAY_REPEAT (Lakehouse v2)
description: ARRAY_REPEAT — 指定した要素を N 回繰り返した配列を作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-repeat.md
---

指定した要素を N 回繰り返した配列を作成します。

## Analyzeの構文

```python
func.array_repeat('x', 3)
```

## Analyzeの例

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## SQLの構文

```sql
ARRAY_REPEAT('x', 3)
```

## SQLの例

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```

---
title: ARRAY_LENGTH (Lakehouse v2)
description: ARRAY_LENGTH — 配列の要素数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-length.md
---

配列の要素数を返します。

## Analyzeの構文

```python
func.array_length([1, 2, 3])
```

## Analyzeの例

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQLの構文

```sql
ARRAY_LENGTH([1, 2, 3])
```

## SQLの例

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```

---
title: "CARDINALITY (配列, Lakehouse v2)"
description: CARDINALITY — 配列の要素数を返します。`ARRAY_LENGTH` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/cardinality.md
---

配列の要素数を返します。`ARRAY_LENGTH` の別名です。

## Analyzeの構文

```python
func.cardinality([1, 2, 3])
```

## Analyzeの例

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQLの構文

```sql
CARDINALITY([1, 2, 3])
```

## SQLの例

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```

---
title: DIVNULL（Lakehouse v1）
description: DIVNULL — 最初の数を 2 番目の数で割った商を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/divnull.md
---

最初の数を 2 番目の数で割った商を返します。2 番目の数が 0 または NULL の場合は NULL を返します。

関連項目：

- [DIV](../div)
- [DIV0](../div0)

## Analyze 構文

```python
func.divnull(<numerator>, <denominator>)
```

## Analyze の例

```python
func.divnull(20, 6), func.divnull(20, 0), func.divnull(20, null)

┌───────────────────────────────────────────────────────────────────┐
│ func.divnull(20, 6)│ func.divnull(20, 0) │ func.divnull(20, null) │
├────────────────────┼─────────────────────┼────────────────────────┤
│ 3.3333333333333335 │ NULL                │ NULL                   │
└───────────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
DIVNULL(<number1>, <number2>)
```

## SQL の例

```sql
SELECT
  DIVNULL(20, 6),
  DIVNULL(20, 0),
  DIVNULL(20, NULL);

┌─────────────────────────────────────────────────────────┐
│   divnull(20, 6)   │ divnull(20, 0) │ divnull(20, null) │
├────────────────────┼────────────────┼───────────────────┤
│ 3.3333333333333335 │ NULL           │ NULL              │
└─────────────────────────────────────────────────────────┘
```

---
title: DIV0（Lakehouse v1）
description: DIV0 — 最初の数を 2 番目の数で割った商を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div0.md
---

最初の数を 2 番目の数で割った商を返します。2 番目の数が 0 の場合は 0 を返します。

関連項目：

- [DIV](../div)
- [DIVNULL](../divnull)

## Analyze 構文

```python
func.div0(<numerator>, <denominator>)
```

## Analyze の例

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
DIV0(<number1>, <number2>)
```

## SQL の例

```sql
SELECT
  DIV0(20, 6),
  DIV0(20, 0),
  DIV0(20, NULL);

┌───────────────────────────────────────────────────┐
│     div0(20, 6)    │ div0(20, 0) │ div0(20, null) │
├────────────────────┼─────────────┼────────────────┤
│ 3.3333333333333335 │           0 │ NULL           │
└───────────────────────────────────────────────────┘
```

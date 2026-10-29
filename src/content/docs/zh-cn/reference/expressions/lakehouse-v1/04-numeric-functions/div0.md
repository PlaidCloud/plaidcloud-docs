---
title: DIV0（Lakehouse v1）
description: DIV0——返回第一个数除以第二个数的商。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div0.md
---

返回第一个数除以第二个数的商。如果第二个数为 0，则返回 0。

另请参阅：

- [DIV](../div)
- [DIVNULL](../divnull)

## Analyze 语法

```python
func.div0(<numerator>, <denominator>)
```

## Analyze 示例

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
DIV0(<number1>, <number2>)
```

## SQL 示例

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

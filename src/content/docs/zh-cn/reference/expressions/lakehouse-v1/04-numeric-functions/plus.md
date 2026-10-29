---
title: PLUS（Lakehouse v1）
description: PLUS——计算两个数值或小数值之和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/plus.md
---

计算两个数值或小数值之和。

## Analyze 语法

```python
func.plus(<number1>, <number2>)
```

## Analyze 示例

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## SQL 语法

```sql
PLUS(<number1>, <number2>)
```

## 别名

- [ADD](../add)

## SQL 示例

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```

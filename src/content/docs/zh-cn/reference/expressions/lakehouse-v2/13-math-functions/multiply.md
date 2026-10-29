---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY — 返回两个数的乘积。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/multiply.md
---

返回两个数的乘积。

## Analyze 语法

```python
func.multiply(<x>, <y>)
```

## Analyze 示例

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## SQL 语法

```sql
MULTIPLY(<x>, <y>)
```

## SQL 示例

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```

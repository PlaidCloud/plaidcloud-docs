---
title: DIVIDE (Lakehouse v2)
description: DIVIDE — 返回一个数除以另一个数的结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

返回一个数除以另一个数的结果。

## Analyze 语法

```python
func.divide(<x>, <y>)
```

## Analyze 示例

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## SQL 语法

```sql
DIVIDE(<x>, <y>)
```

## SQL 示例

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

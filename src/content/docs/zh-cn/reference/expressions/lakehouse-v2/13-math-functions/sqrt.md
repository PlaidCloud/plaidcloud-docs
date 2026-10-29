---
title: SQRT (Lakehouse v2)
description: SQRT — 返回数值的平方根。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sqrt.md
---

返回数值的平方根。

## Analyze 语法

```python
func.sqrt(<x>)
```

## Analyze 示例

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## SQL 语法

```sql
SQRT(<x>)
```

## SQL 示例

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```

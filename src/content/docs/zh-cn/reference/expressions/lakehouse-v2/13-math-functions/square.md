---
title: SQUARE (Lakehouse v2)
description: SQUARE — 返回数值的平方。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

返回数值的平方。

## Analyze 语法

```python
func.square(<x>)
```

## Analyze 示例

```python
func.square(7)

┌────┐
│ 49  │
└────┘
```

## SQL 语法

```sql
SQUARE(<x>)
```

## SQL 示例

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```

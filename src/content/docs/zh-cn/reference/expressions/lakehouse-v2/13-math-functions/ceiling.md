---
title: CEILING (Lakehouse v2)
description: CEILING — 返回大于或等于该数值的最小整数。是 `CEIL` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

返回大于或等于该数值的最小整数。是 `CEIL` 的别名。

## Analyze 语法

```python
func.ceiling(<x>)
```

## Analyze 示例

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## SQL 语法

```sql
CEILING(<x>)
```

## SQL 示例

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```

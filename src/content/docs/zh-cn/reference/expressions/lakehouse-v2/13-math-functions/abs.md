---
title: ABS (Lakehouse v2)
description: ABS — 返回数值的绝对值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

返回数值的绝对值。

## Analyze 语法

```python
func.abs(<x>)
```

## Analyze 示例

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## SQL 语法

```sql
ABS(<x>)
```

## SQL 示例

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```

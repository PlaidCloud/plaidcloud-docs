---
title: FLOOR (Lakehouse v2)
description: FLOOR — 返回小于或等于该数值的最大整数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

返回小于或等于该数值的最大整数。

## Analyze 语法

```python
func.floor(<x>)
```

## Analyze 示例

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## SQL 语法

```sql
FLOOR(<x>)
```

## SQL 示例

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```

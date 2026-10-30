---
title: ROUND (Lakehouse v2)
description: ROUND — 将数值四舍五入到指定的小数位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/round.md
---

将数值四舍五入到指定的小数位数。

## Analyze 语法

```python
func.round(<x>[, <d>])
```

## Analyze 示例

```python
func.round(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQL 语法

```sql
ROUND(<x>[, <d>])
```

## SQL 示例

```sql
SELECT ROUND(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```

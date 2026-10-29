---
title: SINH (Lakehouse v2)
description: SINH — 返回数值的双曲正弦值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

返回数值的双曲正弦值。

## Analyze 语法

```python
func.sinh(<x>)
```

## Analyze 示例

```python
func.sinh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL 语法

```sql
SINH(<x>)
```

## SQL 示例

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```

---
title: SIN (Lakehouse v2)
description: SIN — 返回数值的正弦值（弧度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

返回数值的正弦值（弧度）。

## Analyze 语法

```python
func.sin(<x>)
```

## Analyze 示例

```python
func.sin(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL 语法

```sql
SIN(<x>)
```

## SQL 示例

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```

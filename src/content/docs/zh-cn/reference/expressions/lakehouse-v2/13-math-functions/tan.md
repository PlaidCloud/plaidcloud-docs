---
title: TAN (Lakehouse v2)
description: TAN — 返回数值的正切值（弧度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tan.md
---

返回数值的正切值（弧度）。

## Analyze 语法

```python
func.tan(<x>)
```

## Analyze 示例

```python
func.tan(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL 语法

```sql
TAN(<x>)
```

## SQL 示例

```sql
SELECT TAN(0);

┌─────┐
│ 0.0  │
└─────┘
```

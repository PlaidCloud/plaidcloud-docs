---
title: LN (Lakehouse v2)
description: LN — 返回数值的自然对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

返回数值的自然对数。

## Analyze 语法

```python
func.ln(<x>)
```

## Analyze 示例

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL 语法

```sql
LN(<x>)
```

## SQL 示例

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```

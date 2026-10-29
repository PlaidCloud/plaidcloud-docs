---
title: EXP (Lakehouse v2)
description: EXP — 返回 e 的指定数值次幂。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

返回 e 的指定数值次幂。

## Analyze 语法

```python
func.exp(<x>)
```

## Analyze 示例

```python
func.exp(1)

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

## SQL 语法

```sql
EXP(<x>)
```

## SQL 示例

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

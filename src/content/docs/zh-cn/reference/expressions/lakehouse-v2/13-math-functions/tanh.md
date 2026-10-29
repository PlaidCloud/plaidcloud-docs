---
title: TANH (Lakehouse v2)
description: TANH — 返回数值的双曲正切值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

返回数值的双曲正切值。

## Analyze 语法

```python
func.tanh(<x>)
```

## Analyze 示例

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL 语法

```sql
TANH(<x>)
```

## SQL 示例

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```

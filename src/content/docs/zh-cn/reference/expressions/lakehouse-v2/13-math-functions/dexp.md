---
title: DEXP (Lakehouse v2)
description: DEXP — `EXP` 的别名。参见 [EXP](../exp/)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dexp.md
---

`EXP` 的别名。参见 [EXP](../exp/)。

## Analyze 语法

```python
func.dexp(1)
```

## Analyze 示例

```python
func.dexp(1)

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

## SQL 语法

```sql
DEXP(<x>)
```

## SQL 示例

```sql
SELECT DEXP(1);

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

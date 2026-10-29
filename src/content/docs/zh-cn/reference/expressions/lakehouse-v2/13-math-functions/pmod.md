---
title: PMOD (Lakehouse v2)
description: PMOD — 返回两个数相除的正模数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

返回两个数相除的正模数。

## Analyze 语法

```python
func.pmod(<x>, <y>)
```

## Analyze 示例

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## SQL 语法

```sql
PMOD(<x>, <y>)
```

## SQL 示例

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```

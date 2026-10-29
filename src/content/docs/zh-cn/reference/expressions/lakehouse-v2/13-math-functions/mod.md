---
title: MOD (Lakehouse v2)
description: MOD — 返回两个数相除的余数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

返回两个数相除的余数。

## Analyze 语法

```python
func.mod(<x>, <y>)
```

## Analyze 示例

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
MOD(<x>, <y>)
```

## SQL 示例

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```

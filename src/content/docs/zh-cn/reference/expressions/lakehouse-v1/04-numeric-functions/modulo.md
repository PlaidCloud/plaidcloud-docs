---
title: MODULO（Lakehouse v1）
description: MODULO——返回 x 除以 y 的余数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/modulo.md
---

返回 `x` 除以 `y` 的余数。如果 `y` 为 0，则返回错误。

## Analyze 语法

```python
func.modulo( <x>, <y> )
```

## Analyze 示例

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## SQL 语法

```sql
MODULO( <x>, <y> )
```

## 别名

- [MOD](../mod)

## SQL 示例

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```

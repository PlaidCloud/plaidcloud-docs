---
title: POWER (Lakehouse v2)
description: POWER — 返回一个数的指定次幂。是 `POW` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/power.md
---

返回一个数的指定次幂。是 `POW` 的别名。

## Analyze 语法

```python
func.power(<x>, <y>)
```

## Analyze 示例

```python
func.power(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## SQL 语法

```sql
POWER(<x>, <y>)
```

## SQL 示例

```sql
SELECT POWER(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```

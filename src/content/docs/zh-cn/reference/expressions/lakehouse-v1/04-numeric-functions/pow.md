---
title: POW（Lakehouse v1）
description: POW——返回 x 的 y 次幂。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pow.md
---

返回 `x` 的 `y` 次幂。 

## Analyze 语法

```python
func.pow( <x, y> )
```

## Analyze 示例

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## SQL 语法

```sql
POW( <x, y> )
```

## 别名

- [POWER](../power)

## SQL 示例

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```

---
title: FACTORIAL（Lakehouse v1）
description: FACTORIAL——返回 x 的阶乘对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

返回 `x` 的阶乘对数。如果 `x` 小于或等于 0，则函数返回 0。

## Analyze 语法

```python
func.factorial( <x> )
```

## Analyze 示例

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## SQL 语法

```sql
FACTORIAL( <x> )
```

## SQL 示例

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```

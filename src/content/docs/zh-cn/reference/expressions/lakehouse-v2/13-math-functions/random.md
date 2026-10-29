---
title: RANDOM (Lakehouse v2)
description: RANDOM — 返回介于 0 和 1 之间的随机浮点值。是 `RAND` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

返回介于 0 和 1 之间的随机浮点值。是 `RAND` 的别名。

## Analyze 语法

```python
func.random([<seed>])
```

## Analyze 示例

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## SQL 语法

```sql
RANDOM([<seed>])
```

## SQL 示例

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```

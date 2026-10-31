---
title: POSITIVE (Lakehouse v2)
description: POSITIVE — 原样返回该值（一元加号）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

原样返回该值（一元加号）。

## Analyze 语法

```python
func.positive(<x>)
```

## Analyze 示例

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## SQL 语法

```sql
POSITIVE(<x>)
```

## SQL 示例

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```

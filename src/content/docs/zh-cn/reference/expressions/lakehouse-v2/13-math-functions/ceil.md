---
title: CEIL (Lakehouse v2)
description: CEIL — 返回大于或等于该数值的最小整数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

返回大于或等于该数值的最小整数。

## Analyze 语法

```python
func.ceil(<x>)
```

## Analyze 示例

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## SQL 语法

```sql
CEIL(<x>)
```

## SQL 示例

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```

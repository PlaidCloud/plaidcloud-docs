---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — 返回数值的相反数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

返回数值的相反数。

## Analyze 语法

```python
func.negative(<x>)
```

## Analyze 示例

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## SQL 语法

```sql
NEGATIVE(<x>)
```

## SQL 示例

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```

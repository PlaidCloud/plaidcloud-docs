---
title: WEEK (Lakehouse v2)
description: WEEK — 返回日期在一年中的周数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week.md
---

返回日期在一年中的周数。

## Analyze 语法

```python
func.week(<date>[, <mode>])
```

## Analyze 示例

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL 语法

```sql
WEEK(<date>[, <mode>])
```

## SQL 示例

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```

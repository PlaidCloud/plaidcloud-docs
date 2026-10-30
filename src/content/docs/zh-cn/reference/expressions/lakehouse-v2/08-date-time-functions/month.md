---
title: MONTH (Lakehouse v2)
description: MONTH — 返回日期中的月份。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/month.md
---

返回日期中的月份。

## Analyze 语法

```python
func.month(<date>)
```

## Analyze 示例

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQL 语法

```sql
MONTH(<date>)
```

## SQL 示例

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```

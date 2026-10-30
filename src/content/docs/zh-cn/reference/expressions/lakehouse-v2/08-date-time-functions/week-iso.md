---
title: WEEK_ISO (Lakehouse v2)
description: WEEK_ISO — 返回日期在一年中的 ISO 周数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week-iso.md
---

返回日期在一年中的 ISO 周数。

## Analyze 语法

```python
func.week_iso(<date>)
```

## Analyze 示例

```python
func.week_iso('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL 语法

```sql
WEEK_ISO(<date>)
```

## SQL 示例

```sql
SELECT WEEK_ISO('2024-06-15');

┌────┐
│ 24  │
└────┘
```

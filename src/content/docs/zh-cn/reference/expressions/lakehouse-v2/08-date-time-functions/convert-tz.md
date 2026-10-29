---
title: CONVERT_TZ (Lakehouse v2)
description: CONVERT_TZ：将日期时间从一个时区转换为另一个时区。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/convert-tz.md
---

将日期时间从一个时区转换为另一个时区。

## Analyze 语法

```python
func.convert_tz(<datetime>, <from_tz>, <to_tz>)
```

## Analyze 示例

```python
func.convert_tz('2024-01-01 12:00:00', 'UTC', 'America/New_York')

┌───────────────────────┐
│ '2024-01-01 07:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
CONVERT_TZ(<datetime>, <from_tz>, <to_tz>)
```

## SQL 示例

```sql
SELECT CONVERT_TZ('2024-01-01 12:00:00', 'UTC', 'America/New_York');

┌─────────────────────┐
│ 2024-01-01 07:00:00  │
└─────────────────────┘
```

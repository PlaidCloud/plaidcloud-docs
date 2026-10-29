---
title: TIME_FORMAT (Lakehouse v2)
description: TIME_FORMAT — 按照格式字符串格式化时间值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-format.md
---

按照格式字符串格式化时间值。

## Analyze 语法

```python
func.time_format(<time>, <format>)
```

## Analyze 示例

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## SQL 语法

```sql
TIME_FORMAT(<time>, <format>)
```

## SQL 示例

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```

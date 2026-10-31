---
title: JODATIME_FORMAT (Lakehouse v2)
description: JODATIME_FORMAT：使用 Joda-Time 格式模式格式化日期或日期时间。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/jodatime-format.md
---

使用 Joda-Time 格式模式格式化日期或日期时间。

## Analyze 语法

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Analyze 示例

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQL 语法

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## SQL 示例

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```

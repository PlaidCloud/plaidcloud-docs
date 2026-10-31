---
title: DATE_FORMAT (Lakehouse v2)
description: DATE_FORMAT：根据格式字符串格式化日期或日期时间值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-format.md
---

根据格式字符串格式化日期或日期时间值。

## Analyze 语法

```python
func.date_format(<date>, <format>)
```

## Analyze 示例

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQL 语法

```sql
DATE_FORMAT(<date>, <format>)
```

## SQL 示例

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```

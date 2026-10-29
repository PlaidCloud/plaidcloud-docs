---
title: TO_TERA_TIMESTAMP (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 TO_TERA_TIMESTAMP 日期/时间函数。按照 Teradata 格式字符串将 VARCHAR 值转换为 DATETIME 值。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-timestamp.md
---

按照 Teradata 格式字符串将 VARCHAR 值转换为 DATETIME 值。

## Analyze 语法

```python
func.to_tera_timestamp(<str>, <format>)
```

## Analyze 示例

```python
func.to_tera_timestamp('20240615143000', 'YYYYMMDDHH24MISS')

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
TO_TERA_TIMESTAMP(<str>, <format>)
```

## SQL 示例

```sql
SELECT TO_TERA_TIMESTAMP('20240615143000', 'YYYYMMDDHH24MISS');

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

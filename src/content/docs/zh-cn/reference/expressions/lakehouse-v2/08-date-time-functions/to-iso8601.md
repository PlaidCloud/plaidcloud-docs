---
title: TO_ISO8601 (Lakehouse v2)
description: TO_ISO8601 — 将日期或日期时间值转换为 ISO 8601 格式的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-iso8601.md
---

将日期或日期时间值转换为 ISO 8601 格式的字符串。

## Analyze 语法

```python
func.to_iso8601(<datetime>)
```

## Analyze 示例

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
TO_ISO8601(<datetime>)
```

## SQL 示例

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```

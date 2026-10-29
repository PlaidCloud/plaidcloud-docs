---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — 按照 Teradata 格式字符串将 VARCHAR 值转换为 DATE 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

按照 Teradata 格式字符串将 VARCHAR 值转换为 DATE 值。

## Analyze 语法

```python
func.to_tera_date(<str>, <format>)
```

## Analyze 示例

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 语法

```sql
TO_TERA_DATE(<str>, <format>)
```

## SQL 示例

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

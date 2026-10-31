---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE — 使用格式字符串将字符串解析为日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-date.md
---

使用格式字符串将字符串解析为日期。

## Analyze 语法

```python
func.str_to_date(<str>, <format>)
```

## Analyze 示例

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 语法

```sql
STR_TO_DATE(<str>, <format>)
```

## SQL 示例

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

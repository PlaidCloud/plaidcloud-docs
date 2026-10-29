---
title: DATE_TRUNC (Lakehouse v2)
description: DATE_TRUNC：将日期或日期时间值截断到指定的精度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-trunc.md
---

将日期或日期时间值截断到指定的精度。

## Analyze 语法

```python
func.date_trunc(<unit>, <datetime>)
```

## Analyze 示例

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## SQL 语法

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## SQL 示例

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```

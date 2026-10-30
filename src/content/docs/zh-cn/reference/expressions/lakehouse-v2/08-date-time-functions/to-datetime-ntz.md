---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — 将值转换为不带时区（NTZ）的 DATETIME。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

将值转换为不带时区（NTZ）的 DATETIME。结果不受会话时区设置的影响。

## Analyze 语法

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Analyze 示例

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## SQL 语法

```sql
TO_DATETIME_NTZ(<expr>)
```

## SQL 示例

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

---
title: TO_DATETIME (Lakehouse v2)
description: TO_DATETIME — 将值转换为日期时间值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime.md
---

将值转换为日期时间值。

## Analyze 语法

```python
func.to_datetime(<expr>)
```

## Analyze 示例

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
TO_DATETIME(<expr>)
```

## SQL 示例

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```

---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP — 将日期或字符串转换为日期时间值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestamp.md
---

将日期或字符串转换为日期时间值。

## Analyze 语法

```python
func.timestamp(<expr>)
```

## Analyze 示例

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
TIMESTAMP(<expr>)
```

## SQL 示例

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```

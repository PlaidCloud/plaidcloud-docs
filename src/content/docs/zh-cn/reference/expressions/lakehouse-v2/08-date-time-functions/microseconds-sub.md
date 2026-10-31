---
title: MICROSECONDS_SUB (Lakehouse v2)
description: MICROSECONDS_SUB — 从日期时间值中减去指定的微秒数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-sub.md
---

从日期时间值中减去指定的微秒数。

## Analyze 语法

```python
func.microseconds_sub(<datetime>, <n>)
```

## Analyze 示例

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## SQL 示例

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```

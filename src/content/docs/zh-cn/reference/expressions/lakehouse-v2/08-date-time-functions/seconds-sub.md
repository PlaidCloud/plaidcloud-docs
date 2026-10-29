---
title: SECONDS_SUB (Lakehouse v2)
description: SECONDS_SUB — 从日期时间值中减去指定的秒数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-sub.md
---

从日期时间值中减去指定的秒数。

## Analyze 语法

```python
func.seconds_sub(<datetime>, <n>)
```

## Analyze 示例

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
SECONDS_SUB(<datetime>, <n>)
```

## SQL 示例

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```

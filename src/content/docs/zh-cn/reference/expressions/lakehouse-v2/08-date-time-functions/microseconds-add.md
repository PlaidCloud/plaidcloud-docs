---
title: MICROSECONDS_ADD (Lakehouse v2)
description: MICROSECONDS_ADD — 为日期时间值加上指定的微秒数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-add.md
---

为日期时间值加上指定的微秒数。

## Analyze 语法

```python
func.microseconds_add(<datetime>, <n>)
```

## Analyze 示例

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## SQL 语法

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## SQL 示例

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```

---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD — 为日期时间值加上指定的秒数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

为日期时间值加上指定的秒数。

## Analyze 语法

```python
func.seconds_add(<datetime>, <n>)
```

## Analyze 示例

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## SQL 语法

```sql
SECONDS_ADD(<datetime>, <n>)
```

## SQL 示例

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```

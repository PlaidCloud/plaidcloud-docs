---
title: TIMESTAMPADD (Lakehouse v2)
description: TIMESTAMPADD — 为日期时间值加上指定的时间间隔。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampadd.md
---

为日期时间值加上指定的时间间隔。

## Analyze 语法

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Analyze 示例

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQL 语法

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## SQL 示例

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```

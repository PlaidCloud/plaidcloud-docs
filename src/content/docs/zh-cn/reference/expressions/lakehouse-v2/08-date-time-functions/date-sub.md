---
title: DATE_SUB (Lakehouse v2)
description: DATE_SUB：从日期或日期时间中减去指定的时间间隔。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-sub.md
---

从日期或日期时间中减去指定的时间间隔。

## Analyze 语法

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Analyze 示例

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## SQL 语法

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## SQL 示例

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```

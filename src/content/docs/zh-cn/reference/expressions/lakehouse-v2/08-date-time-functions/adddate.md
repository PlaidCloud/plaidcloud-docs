---
title: ADDDATE (Lakehouse v2)
description: ADDDATE：为日期加上指定的时间间隔，是 `DATE_ADD` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/adddate.md
---

为日期加上指定的时间间隔，是 `DATE_ADD` 的别名。

## Analyze 语法

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Analyze 示例

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQL 语法

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## SQL 示例

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```

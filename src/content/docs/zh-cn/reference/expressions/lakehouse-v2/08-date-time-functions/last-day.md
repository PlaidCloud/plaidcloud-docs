---
title: LAST_DAY (Lakehouse v2)
description: LAST_DAY：返回给定日期所在月份的最后一天。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/last-day.md
---

返回给定日期所在月份的最后一天。

## Analyze 语法

```python
func.last_day(<date>[, <unit>])
```

## Analyze 示例

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQL 语法

```sql
LAST_DAY(<date>[, <unit>])
```

## SQL 示例

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```

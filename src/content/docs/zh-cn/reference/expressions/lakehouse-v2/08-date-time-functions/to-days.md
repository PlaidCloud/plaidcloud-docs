---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS — 将日期转换为天数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-days.md
---

将日期转换为天数。

## Analyze 语法

```python
func.to_days(<date>)
```

## Analyze 示例

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## SQL 语法

```sql
TO_DAYS(<date>)
```

## SQL 示例

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```

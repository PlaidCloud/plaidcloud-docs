---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS：将天数转换为日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-days.md
---

将天数转换为日期。

## Analyze 语法

```python
func.from_days(<n>)
```

## Analyze 示例

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL 语法

```sql
FROM_DAYS(<n>)
```

## SQL 示例

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```

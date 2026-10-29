---
title: HOUR (Lakehouse v2)
description: HOUR：返回日期时间中的小时。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hour.md
---

返回日期时间中的小时。

## Analyze 语法

```python
func.hour(<datetime>)
```

## Analyze 示例

```python
func.hour('2024-06-15 14:30:00')

┌────┐
│ 14  │
└────┘
```

## SQL 语法

```sql
HOUR(<datetime>)
```

## SQL 示例

```sql
SELECT HOUR('2024-06-15 14:30:00');

┌────┐
│ 14  │
└────┘
```

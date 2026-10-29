---
title: MINUTE (Lakehouse v2)
description: MINUTE — 返回日期时间值中的分钟部分。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

返回日期时间值中的分钟部分。

## Analyze 语法

```python
func.minute(<datetime>)
```

## Analyze 示例

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## SQL 语法

```sql
MINUTE(<datetime>)
```

## SQL 示例

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```

---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE：返回当前日期，是 `CURDATE` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-date.md
---

返回当前日期，是 `CURDATE` 的别名。

## Analyze 语法

```python
func.current_date()
```

## Analyze 示例

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 语法

```sql
CURRENT_DATE()
```

## SQL 示例

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

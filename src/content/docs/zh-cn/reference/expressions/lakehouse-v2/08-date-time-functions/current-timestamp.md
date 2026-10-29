---
title: CURRENT_TIMESTAMP (Lakehouse v2)
description: CURRENT_TIMESTAMP：返回当前日期和时间。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timestamp.md
---

返回当前日期和时间。

## Analyze 语法

```python
func.current_timestamp()
```

## Analyze 示例

```python
func.current_timestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
CURRENT_TIMESTAMP()
```

## SQL 示例

```sql
SELECT CURRENT_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

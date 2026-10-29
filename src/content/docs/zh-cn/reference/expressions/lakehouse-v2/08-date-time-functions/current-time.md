---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME：返回当前时间。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-time.md
---

返回当前时间。

## Analyze 语法

```python
func.current_time()
```

## Analyze 示例

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL 语法

```sql
CURRENT_TIME()
```

## SQL 示例

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```

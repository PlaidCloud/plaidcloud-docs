---
title: UTC_TIME (Lakehouse v2)
description: UTC_TIME — 返回当前 UTC 时间。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-time.md
---

返回当前 UTC 时间。

## Analyze 语法

```python
func.utc_time()
```

## Analyze 示例

```python
func.utc_time()

┌────────────┐
│ '18:30:00'  │
└────────────┘
```

## SQL 语法

```sql
UTC_TIME()
```

## SQL 示例

```sql
SELECT UTC_TIME();

┌──────────┐
│ 18:30:00  │
└──────────┘
```

---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP — 返回当前 UTC 日期和时间。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

返回当前 UTC 日期和时间。

## Analyze 语法

```python
func.utc_timestamp()
```

## Analyze 示例

```python
func.utc_timestamp()

┌───────────────────────┐
│ '2024-06-15 18:30:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
UTC_TIMESTAMP()
```

## SQL 示例

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```

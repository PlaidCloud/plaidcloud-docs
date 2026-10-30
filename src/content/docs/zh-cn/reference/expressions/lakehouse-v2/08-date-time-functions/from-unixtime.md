---
title: FROM_UNIXTIME (Lakehouse v2)
description: FROM_UNIXTIME：将 Unix 时间戳转换为日期时间字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-unixtime.md
---

将 Unix 时间戳转换为日期时间字符串。

## Analyze 语法

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Analyze 示例

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## SQL 示例

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```

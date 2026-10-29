---
title: UNIX_TIMESTAMP (Lakehouse v2)
description: UNIX_TIMESTAMP — 将日期时间值转换为 Unix 时间戳。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/unix-timestamp.md
---

将日期时间值转换为 Unix 时间戳。

## Analyze 语法

```python
func.unix_timestamp([<datetime>])
```

## Analyze 示例

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## SQL 语法

```sql
UNIX_TIMESTAMP([<datetime>])
```

## SQL 示例

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```

---
title: SEC_TO_TIME (Lakehouse v2)
description: SEC_TO_TIME — 将秒数转换为时间值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/sec-to-time.md
---

将秒数转换为时间值。

## Analyze 语法

```python
func.sec_to_time(<seconds>)
```

## Analyze 示例

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## SQL 语法

```sql
SEC_TO_TIME(<seconds>)
```

## SQL 示例

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```

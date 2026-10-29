---
title: CURRENT_TIMEZONE (Lakehouse v2)
description: CURRENT_TIMEZONE：返回当前会话的时区。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timezone.md
---

返回当前会话的时区。

## Analyze 语法

```python
func.current_timezone()
```

## Analyze 示例

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## SQL 语法

```sql
CURRENT_TIMEZONE()
```

## SQL 示例

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```

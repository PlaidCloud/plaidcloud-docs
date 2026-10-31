---
title: CURTIME (Lakehouse v2)
description: CURTIME：返回当前时间，是 `CURRENT_TIME` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curtime.md
---

返回当前时间，是 `CURRENT_TIME` 的别名。

## Analyze 语法

```python
func.curtime()
```

## Analyze 示例

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL 语法

```sql
CURTIME()
```

## SQL 示例

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```

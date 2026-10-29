---
title: LOCALTIME (Lakehouse v2)
description: LOCALTIME：返回当前日期和时间，是 `NOW` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtime.md
---

返回当前日期和时间，是 `NOW` 的别名。

## Analyze 语法

```python
func.localtime()
```

## Analyze 示例

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
LOCALTIME()
```

## SQL 示例

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

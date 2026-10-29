---
title: LOCALTIMESTAMP (Lakehouse v2)
description: LOCALTIMESTAMP：返回当前日期和时间，是 `NOW` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtimestamp.md
---

返回当前日期和时间，是 `NOW` 的别名。

## Analyze 语法

```python
func.localtimestamp()
```

## Analyze 示例

```python
func.localtimestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
LOCALTIMESTAMP()
```

## SQL 示例

```sql
SELECT LOCALTIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

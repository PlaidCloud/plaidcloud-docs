---
title: NOW (Lakehouse v2)
description: NOW — 返回当前日期和时间。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

返回当前日期和时间。

## Analyze 语法

```python
func.now()
```

## Analyze 示例

```python
func.now()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
NOW()
```

## SQL 示例

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

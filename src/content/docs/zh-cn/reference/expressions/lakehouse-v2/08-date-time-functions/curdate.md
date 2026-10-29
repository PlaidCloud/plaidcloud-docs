---
title: CURDATE (Lakehouse v2)
description: CURDATE：返回当前日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curdate.md
---

返回当前日期。

## Analyze 语法

```python
func.curdate()
```

## Analyze 示例

```python
func.curdate()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 语法

```sql
CURDATE()
```

## SQL 示例

```sql
SELECT CURDATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

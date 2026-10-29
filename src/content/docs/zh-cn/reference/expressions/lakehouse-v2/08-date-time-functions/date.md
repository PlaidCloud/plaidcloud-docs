---
title: DATE (Lakehouse v2)
description: DATE：从日期时间表达式中提取日期部分。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date.md
---

从日期时间表达式中提取日期部分。

## Analyze 语法

```python
func.date(<datetime>)
```

## Analyze 示例

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 语法

```sql
DATE(<datetime>)
```

## SQL 示例

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

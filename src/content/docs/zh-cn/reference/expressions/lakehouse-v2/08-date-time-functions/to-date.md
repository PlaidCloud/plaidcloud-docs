---
title: TO_DATE (Lakehouse v2)
description: TO_DATE — 将日期时间值转换为日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

将日期时间值转换为日期。

## Analyze 语法

```python
func.to_date(<datetime>)
```

## Analyze 示例

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 语法

```sql
TO_DATE(<datetime>)
```

## SQL 示例

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

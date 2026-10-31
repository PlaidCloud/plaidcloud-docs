---
title: SECOND (Lakehouse v2)
description: SECOND — 返回日期时间值中的秒部分。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

返回日期时间值中的秒部分。

## Analyze 语法

```python
func.second(<datetime>)
```

## Analyze 示例

```python
func.second('2024-06-15 14:30:45')

┌────┐
│ 45  │
└────┘
```

## SQL 语法

```sql
SECOND(<datetime>)
```

## SQL 示例

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```

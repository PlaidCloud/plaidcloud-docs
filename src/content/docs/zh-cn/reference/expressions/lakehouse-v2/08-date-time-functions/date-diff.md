---
title: DATE_DIFF (Lakehouse v2)
description: DATE_DIFF：按指定单位返回两个日期之间的差值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-diff.md
---

按指定单位返回两个日期之间的差值。

## Analyze 语法

```python
func.date_diff(<unit>, <start>, <end>)
```

## Analyze 示例

```python
func.date_diff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQL 语法

```sql
DATE_DIFF(<unit>, <start>, <end>)
```

## SQL 示例

```sql
SELECT DATE_DIFF('DAY', '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```

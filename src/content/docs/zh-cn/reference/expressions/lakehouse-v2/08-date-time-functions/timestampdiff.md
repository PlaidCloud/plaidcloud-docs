---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — 以指定单位返回两个日期时间值之间的差值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

以指定单位返回两个日期时间值之间的差值。

## Analyze 语法

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Analyze 示例

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQL 语法

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## SQL 示例

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```

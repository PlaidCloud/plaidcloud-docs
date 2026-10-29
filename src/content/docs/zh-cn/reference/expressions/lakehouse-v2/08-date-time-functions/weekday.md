---
title: WEEKDAY (Lakehouse v2)
description: WEEKDAY — 返回日期对应的星期索引（0=星期一，6=星期日）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekday.md
---

返回日期对应的星期索引（0=星期一，6=星期日）。

## Analyze 语法

```python
func.weekday(<date>)
```

## Analyze 示例

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## SQL 语法

```sql
WEEKDAY(<date>)
```

## SQL 示例

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```

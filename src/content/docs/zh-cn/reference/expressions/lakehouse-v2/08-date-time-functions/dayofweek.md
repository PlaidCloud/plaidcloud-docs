---
title: DAYOFWEEK (Lakehouse v2)
description: DAYOFWEEK：返回日期的星期索引（1=星期日，7=星期六）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek.md
---

返回日期的星期索引（1=星期日，7=星期六）。

## Analyze 语法

```python
func.dayofweek(<date>)
```

## Analyze 示例

```python
func.dayofweek('2024-06-15')

┌───┐
│ 7  │
└───┘
```

## SQL 语法

```sql
DAYOFWEEK(<date>)
```

## SQL 示例

```sql
SELECT DAYOFWEEK('2024-06-15');

┌───┐
│ 7  │
└───┘
```

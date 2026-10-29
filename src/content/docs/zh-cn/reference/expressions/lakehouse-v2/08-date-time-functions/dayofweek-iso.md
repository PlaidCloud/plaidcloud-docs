---
title: DAYOFWEEK_ISO (Lakehouse v2)
description: DAYOFWEEK_ISO：返回日期的 ISO 星期索引（1=星期一，7=星期日）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek-iso.md
---

返回日期的 ISO 星期索引（1=星期一，7=星期日）。

## Analyze 语法

```python
func.dayofweek_iso(<date>)
```

## Analyze 示例

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQL 语法

```sql
DAYOFWEEK_ISO(<date>)
```

## SQL 示例

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```

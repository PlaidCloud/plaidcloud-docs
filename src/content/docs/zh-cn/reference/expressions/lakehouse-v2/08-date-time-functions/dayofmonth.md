---
title: DAYOFMONTH (Lakehouse v2)
description: DAYOFMONTH：返回日期中的月内日，是 `DAY` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofmonth.md
---

返回日期中的月内日，是 `DAY` 的别名。

## Analyze 语法

```python
func.dayofmonth(<date>)
```

## Analyze 示例

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQL 语法

```sql
DAYOFMONTH(<date>)
```

## SQL 示例

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```

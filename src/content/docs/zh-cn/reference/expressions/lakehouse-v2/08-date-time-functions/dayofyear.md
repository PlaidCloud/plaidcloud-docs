---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR：返回日期在一年中的第几天。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofyear.md
---

返回日期在一年中的第几天。

## Analyze 语法

```python
func.dayofyear(<date>)
```

## Analyze 示例

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## SQL 语法

```sql
DAYOFYEAR(<date>)
```

## SQL 示例

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```

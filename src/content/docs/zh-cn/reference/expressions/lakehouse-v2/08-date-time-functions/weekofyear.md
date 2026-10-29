---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR — 返回日期在一年中的周数。是 `WEEK` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekofyear.md
---

返回日期在一年中的周数。是 `WEEK` 的别名。

## Analyze 语法

```python
func.weekofyear(<date>)
```

## Analyze 示例

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL 语法

```sql
WEEKOFYEAR(<date>)
```

## SQL 示例

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```

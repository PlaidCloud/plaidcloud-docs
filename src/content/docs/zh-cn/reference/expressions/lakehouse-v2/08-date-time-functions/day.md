---
title: DAY (Lakehouse v2)
description: DAY：返回日期中的月内日。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/day.md
---

返回日期中的月内日。

## Analyze 语法

```python
func.day(<date>)
```

## Analyze 示例

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQL 语法

```sql
DAY(<date>)
```

## SQL 示例

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```

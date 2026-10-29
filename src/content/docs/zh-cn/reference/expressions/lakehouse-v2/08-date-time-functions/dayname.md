---
title: DAYNAME (Lakehouse v2)
description: DAYNAME：返回日期对应的星期名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayname.md
---

返回日期对应的星期名称。

## Analyze 语法

```python
func.dayname(<date>)
```

## Analyze 示例

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## SQL 语法

```sql
DAYNAME(<date>)
```

## SQL 示例

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```

---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME — 返回日期所在月份的名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

返回日期所在月份的名称。

## Analyze 语法

```python
func.monthname(<date>)
```

## Analyze 示例

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## SQL 语法

```sql
MONTHNAME(<date>)
```

## SQL 示例

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```

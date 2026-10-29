---
title: IFNULL (Lakehouse v2)
description: IFNULL：如果第一个表达式不为 NULL，则返回它，否则返回第二个表达式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/ifnull.md
---

如果第一个表达式不为 NULL，则返回它，否则返回第二个表达式。

## Analyze 语法

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Analyze 示例

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## SQL 语法

```sql
IFNULL(<phone>, 'N/A')
```

## SQL 示例

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```

---
title: COALESCE (Lakehouse v2)
description: COALESCE：从表达式列表中返回第一个非 NULL 的表达式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/coalesce.md
---

从表达式列表中返回第一个非 NULL 的表达式。

## Analyze 语法

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Analyze 示例

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## SQL 语法

```sql
COALESCE(<nickname>, <name>)
```

## SQL 示例

```sql
SELECT COALESCE(nickname, first_name, 'Unknown') AS display_name FROM users;

┌──────────────┐
│ display_name │
├──────────────┤
│ Bob          │
│ Alice        │
│ Unknown      │
└──────────────┘
```

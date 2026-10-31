---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE：返回列值序列化形式的字节大小。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

返回列值序列化形式的字节大小。

## Analyze 语法

```python
func.column_size(get_column(table, 'name'))
```

## Analyze 示例

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## SQL 语法

```sql
COLUMN_SIZE(<expr>)
```

## SQL 示例

```sql
SELECT name, COLUMN_SIZE(name) FROM users LIMIT 3;

┌──────���┬───────────────────┐
│ name  │ column_size(name) │
├───────┼───────────────────┤
│ Alice │                 5 │
│ Bob   │                 3 │
│ Eve   │                 3 │
└───────┴───────────────────┘
```

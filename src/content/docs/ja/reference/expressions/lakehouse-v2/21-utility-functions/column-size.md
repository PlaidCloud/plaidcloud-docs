---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE — 列の値のシリアル化された形式でのサイズをバイト単位で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

列の値のシリアル化された形式でのサイズをバイト単位で返します。

## Analyze 構文

```python
func.column_size(get_column(table, 'name'))
```

## Analyze の例

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## SQL 構文

```sql
COLUMN_SIZE(<expr>)
```

## SQL の例

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

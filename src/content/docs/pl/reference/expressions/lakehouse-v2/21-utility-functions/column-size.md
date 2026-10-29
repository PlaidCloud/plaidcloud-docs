---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE — zwraca rozmiar wartości kolumny w bajtach w jej postaci zserializowanej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

Zwraca rozmiar wartości kolumny w bajtach w jej postaci zserializowanej.

## Składnia Analyze

```python
func.column_size(get_column(table, 'name'))
```

## Przykłady Analyze

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## Składnia SQL

```sql
COLUMN_SIZE(<expr>)
```

## Przykłady SQL

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

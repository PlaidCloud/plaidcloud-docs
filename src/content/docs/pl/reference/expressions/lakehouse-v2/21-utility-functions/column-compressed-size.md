---
title: COLUMN_COMPRESSED_SIZE (Lakehouse v2)
description: COLUMN_COMPRESSED_SIZE — zwraca skompresowany rozmiar wartości kolumny w bajtach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-compressed-size.md
---

Zwraca skompresowany rozmiar wartości kolumny w bajtach.

## Składnia Analyze

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Przykłady Analyze

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## Składnia SQL

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## Przykłady SQL

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```

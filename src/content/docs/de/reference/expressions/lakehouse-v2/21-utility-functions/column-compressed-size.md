---
title: COLUMN_COMPRESSED_SIZE (Lakehouse v2)
description: COLUMN_COMPRESSED_SIZE — gibt die komprimierte Größe eines Spaltenwerts in Bytes zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-compressed-size.md
---

Gibt die komprimierte Größe eines Spaltenwerts in Bytes zurück.

## Analyze-Syntax

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Analyze-Beispiele

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## SQL-Syntax

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## SQL-Beispiele

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```

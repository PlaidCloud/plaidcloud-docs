---
title: COLUMN_COMPRESSED_SIZE
---

Returns the compressed size in bytes of a column value.

## Analyze Syntax

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Analyze Examples

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## SQL Syntax

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## SQL Examples

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```

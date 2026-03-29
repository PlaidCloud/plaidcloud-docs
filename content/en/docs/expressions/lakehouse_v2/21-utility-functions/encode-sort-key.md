---
title: ENCODE_SORT_KEY
---

Encodes values into a binary sort key that preserves the sort order. Useful for compound sort keys.

## Analyze Syntax

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Analyze Examples

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## SQL Syntax

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## SQL Examples

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```

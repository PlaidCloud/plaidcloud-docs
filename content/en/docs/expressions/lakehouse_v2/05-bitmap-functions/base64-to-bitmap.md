---
title: BASE64_TO_BITMAP
---

Converts a base64-encoded string to a bitmap.

## Analyze Syntax

```python
func.base64_to_bitmap(<str>)
```

## Analyze Examples

```python
func.base64_to_bitmap(get_column(table, 'b64_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL Syntax

```sql
BASE64_TO_BITMAP(<str>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_STRING(BASE64_TO_BITMAP(b64_col)) FROM data;

┌───────┐
│ 1,2,3 │
└───────┘
```

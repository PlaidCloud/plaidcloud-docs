---
title: BITMAP_TO_BASE64
description: BITMAP_TO_BASE64 — Converts a bitmap to a base64-encoded string.
---

Converts a bitmap to a base64-encoded string.

## Analyze Syntax

```python
func.bitmap_to_base64(<bitmap>)
```

## Analyze Examples

```python
func.bitmap_to_base64(get_column(table, 'bm'))

┌──────────┐
│ 'AQI...' │
└──────────┘
```

## SQL Syntax

```sql
BITMAP_TO_BASE64(<bitmap>)
```

## SQL Examples

```sql
SELECT BITMAP_TO_BASE64(BITMAP_FROM_STRING('1,2,3'));

┌─────────────────┐
│ (base64 string) │
└─────────────────┘
```

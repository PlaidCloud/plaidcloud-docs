---
title: PARSE_URL (Lakehouse v2)
description: PARSE_URL — extracts a specified part from a URL string.
---

Extracts a specified part from a URL string.

## Analyze Syntax

```python
func.parse_url(<url>, <part>)
```

## Analyze Examples

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## SQL Syntax

```sql
PARSE_URL(<url>, <part>)
```

## SQL Examples

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```

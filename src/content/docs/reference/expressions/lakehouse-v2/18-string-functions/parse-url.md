---
title: PARSE_URL
description: "Learn how to use the PARSE_URL string function in PlaidCloud Lakehouse. Extracts a specified part from a URL string - see syntax, examples, and output."
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

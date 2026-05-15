---
title: URL_EXTRACT_PARAMETER
description: URL_EXTRACT_PARAMETER — extracts the value of a query parameter from a URL string.
---

Extracts the value of a query parameter from a URL string.

## Analyze Syntax

```python
func.url_extract_parameter(<url>, <param>)
```

## Analyze Examples

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## SQL Syntax

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## SQL Examples

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```

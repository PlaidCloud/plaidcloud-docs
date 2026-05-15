---
title: URL_DECODE
description: URL_DECODE — decodes a URL-encoded string - see syntax, examples, and output.
---

Decodes a URL-encoded string.

## Analyze Syntax

```python
func.url_decode(<str>)
```

## Analyze Examples

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL Syntax

```sql
URL_DECODE(<str>)
```

## SQL Examples

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```

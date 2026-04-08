---
title: URL_ENCODE
description: "Learn how to use the URL_ENCODE string function in PlaidCloud Lakehouse. Encodes a string for use in a URL - see syntax, examples, and output."
---

Encodes a string for use in a URL.

## Analyze Syntax

```python
func.url_encode(<str>)
```

## Analyze Examples

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## SQL Syntax

```sql
URL_ENCODE(<str>)
```

## SQL Examples

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```

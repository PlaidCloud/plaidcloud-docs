---
title: URL_ENCODE (Lakehouse v2)
description: URL_ENCODE — encodes a string for use in a URL.
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

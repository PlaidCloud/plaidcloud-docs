---
title: URL_EXTRACT_HOST
description: "Learn how to use the URL_EXTRACT_HOST string function in PlaidCloud Lakehouse. Extracts the host from a URL string - see syntax, examples, and output."
---

Extracts the host from a URL string.

## Analyze Syntax

```python
func.url_extract_host(<url>)
```

## Analyze Examples

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## SQL Syntax

```sql
URL_EXTRACT_HOST(<url>)
```

## SQL Examples

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```

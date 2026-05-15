---
title: URL_EXTRACT_HOST (Lakehouse v2)
description: URL_EXTRACT_HOST — extracts the host from a URL string.
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

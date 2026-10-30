---
title: URL_EXTRACT_HOST (Lakehouse v2)
description: URL_EXTRACT_HOST — extrahiert den Host aus einer URL-Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-host.md
---

Extrahiert den Host aus einer URL-Zeichenfolge.

## Analyze-Syntax

```python
func.url_extract_host(<url>)
```

## Analyze-Beispiele

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## SQL-Syntax

```sql
URL_EXTRACT_HOST(<url>)
```

## SQL-Beispiele

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```

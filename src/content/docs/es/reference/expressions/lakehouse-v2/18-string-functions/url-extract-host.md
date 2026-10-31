---
title: URL_EXTRACT_HOST (Lakehouse v2)
description: URL_EXTRACT_HOST — Extrae el host de una cadena de URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-host.md
---

Extrae el host de una cadena de URL.

## Sintaxis de Analyze

```python
func.url_extract_host(<url>)
```

## Ejemplos de Analyze

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
URL_EXTRACT_HOST(<url>)
```

## Ejemplos de SQL

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```

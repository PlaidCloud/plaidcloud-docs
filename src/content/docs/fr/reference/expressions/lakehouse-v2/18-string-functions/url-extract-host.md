---
title: URL_EXTRACT_HOST (Lakehouse v2)
description: URL_EXTRACT_HOST — extrait l'hôte d'une chaîne d'URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-host.md
---

Extrait l'hôte d'une chaîne d'URL.

## Syntaxe Analyze

```python
func.url_extract_host(<url>)
```

## Exemples Analyze

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## Syntaxe SQL

```sql
URL_EXTRACT_HOST(<url>)
```

## Exemples SQL

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```

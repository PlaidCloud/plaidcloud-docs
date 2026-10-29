---
title: URL_EXTRACT_HOST (Lakehouse v2)
description: URL_EXTRACT_HOST — wyodrębnia host z ciągu z adresem URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-host.md
---

Wyodrębnia host z ciągu z adresem URL.

## Składnia Analyze

```python
func.url_extract_host(<url>)
```

## Przykłady Analyze

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## Składnia SQL

```sql
URL_EXTRACT_HOST(<url>)
```

## Przykłady SQL

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```

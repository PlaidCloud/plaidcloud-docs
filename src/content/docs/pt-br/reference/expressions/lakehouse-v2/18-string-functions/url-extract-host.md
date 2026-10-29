---
title: URL_EXTRACT_HOST (Lakehouse v2)
description: URL_EXTRACT_HOST — extrai o host de uma string de URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-host.md
---

Extrai o host de uma string de URL.

## Sintaxe do Analyze

```python
func.url_extract_host(<url>)
```

## Exemplos do Analyze

```python
func.url_extract_host('https://docs.starrocks.io/path')

┌─────────────────────┐
│ 'docs.starrocks.io'  │
└─────────────────────┘
```

## Sintaxe SQL

```sql
URL_EXTRACT_HOST(<url>)
```

## Exemplos de SQL

```sql
SELECT URL_EXTRACT_HOST('https://docs.starrocks.io/path');

┌───────────────────┐
│ docs.starrocks.io  │
└───────────────────┘
```

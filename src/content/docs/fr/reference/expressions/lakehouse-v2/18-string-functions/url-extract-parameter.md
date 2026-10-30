---
title: URL_EXTRACT_PARAMETER (Lakehouse v2)
description: URL_EXTRACT_PARAMETER — extrait la valeur d'un paramètre de requête d'une chaîne d'URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-parameter.md
---

Extrait la valeur d'un paramètre de requête d'une chaîne d'URL.

## Syntaxe Analyze

```python
func.url_extract_parameter(<url>, <param>)
```

## Exemples Analyze

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## Syntaxe SQL

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## Exemples SQL

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```

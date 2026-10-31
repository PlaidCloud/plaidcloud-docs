---
title: URL_EXTRACT_PARAMETER (Lakehouse v2)
description: URL_EXTRACT_PARAMETER — wyodrębnia wartość parametru zapytania z ciągu z adresem URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-parameter.md
---

Wyodrębnia wartość parametru zapytania z ciągu z adresem URL.

## Składnia Analyze

```python
func.url_extract_parameter(<url>, <param>)
```

## Przykłady Analyze

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## Składnia SQL

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## Przykłady SQL

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```

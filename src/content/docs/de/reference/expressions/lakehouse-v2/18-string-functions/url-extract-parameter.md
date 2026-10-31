---
title: URL_EXTRACT_PARAMETER (Lakehouse v2)
description: URL_EXTRACT_PARAMETER — extrahiert den Wert eines Abfrageparameters aus einer URL-Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-parameter.md
---

Extrahiert den Wert eines Abfrageparameters aus einer URL-Zeichenfolge.

## Analyze-Syntax

```python
func.url_extract_parameter(<url>, <param>)
```

## Analyze-Beispiele

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## SQL-Syntax

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## SQL-Beispiele

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```

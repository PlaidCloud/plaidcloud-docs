---
title: URL_EXTRACT_PARAMETER (Lakehouse v2)
description: URL_EXTRACT_PARAMETER — Extrae el valor de un parámetro de consulta de una cadena de URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-parameter.md
---

Extrae el valor de un parámetro de consulta de una cadena de URL.

## Sintaxis de Analyze

```python
func.url_extract_parameter(<url>, <param>)
```

## Ejemplos de Analyze

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## Sintaxis de SQL

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## Ejemplos de SQL

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```

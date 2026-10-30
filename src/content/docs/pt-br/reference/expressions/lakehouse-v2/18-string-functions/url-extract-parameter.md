---
title: URL_EXTRACT_PARAMETER (Lakehouse v2)
description: URL_EXTRACT_PARAMETER — extrai o valor de um parâmetro de consulta de uma string de URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-extract-parameter.md
---

Extrai o valor de um parâmetro de consulta de uma string de URL.

## Sintaxe do Analyze

```python
func.url_extract_parameter(<url>, <param>)
```

## Exemplos do Analyze

```python
func.url_extract_parameter('https://example.com?page=1&size=10', 'page')

┌─────┐
│ '1'  │
└─────┘
```

## Sintaxe SQL

```sql
URL_EXTRACT_PARAMETER(<url>, <param>)
```

## Exemplos de SQL

```sql
SELECT URL_EXTRACT_PARAMETER('https://example.com?page=1&size=10', 'page');

┌───┐
│ 1  │
└───┘
```

---
title: URL_DECODE (Lakehouse v2)
description: URL_DECODE — Decodifica una cadena codificada como URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

Decodifica una cadena codificada como URL.

## Sintaxis de Analyze

```python
func.url_decode(<str>)
```

## Ejemplos de Analyze

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
URL_DECODE(<str>)
```

## Ejemplos de SQL

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```

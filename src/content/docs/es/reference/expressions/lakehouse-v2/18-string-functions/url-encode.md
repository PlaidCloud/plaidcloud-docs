---
title: URL_ENCODE (Lakehouse v2)
description: URL_ENCODE — Codifica una cadena para usarla en una URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-encode.md
---

Codifica una cadena para usarla en una URL.

## Sintaxis de Analyze

```python
func.url_encode(<str>)
```

## Ejemplos de Analyze

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## Sintaxis de SQL

```sql
URL_ENCODE(<str>)
```

## Ejemplos de SQL

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```

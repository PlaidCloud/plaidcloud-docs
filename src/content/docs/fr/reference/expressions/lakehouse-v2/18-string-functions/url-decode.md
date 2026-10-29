---
title: URL_DECODE (Lakehouse v2)
description: URL_DECODE — décode une chaîne encodée pour une URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

Décode une chaîne encodée pour une URL.

## Syntaxe Analyze

```python
func.url_decode(<str>)
```

## Exemples Analyze

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## Syntaxe SQL

```sql
URL_DECODE(<str>)
```

## Exemples SQL

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```

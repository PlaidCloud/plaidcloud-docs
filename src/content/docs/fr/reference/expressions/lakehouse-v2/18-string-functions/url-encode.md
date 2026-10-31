---
title: URL_ENCODE (Lakehouse v2)
description: URL_ENCODE — encode une chaîne pour l'utiliser dans une URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-encode.md
---

Encode une chaîne pour l'utiliser dans une URL.

## Syntaxe Analyze

```python
func.url_encode(<str>)
```

## Exemples Analyze

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## Syntaxe SQL

```sql
URL_ENCODE(<str>)
```

## Exemples SQL

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```

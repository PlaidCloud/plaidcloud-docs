---
title: URL_ENCODE (Lakehouse v2)
description: URL_ENCODE — codifica uma string para uso em uma URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-encode.md
---

Codifica uma string para uso em uma URL.

## Sintaxe do Analyze

```python
func.url_encode(<str>)
```

## Exemplos do Analyze

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## Sintaxe SQL

```sql
URL_ENCODE(<str>)
```

## Exemplos de SQL

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```

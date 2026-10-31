---
title: URL_DECODE (Lakehouse v2)
description: URL_DECODE — decodifica uma string codificada como URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

Decodifica uma string codificada como URL.

## Sintaxe do Analyze

```python
func.url_decode(<str>)
```

## Exemplos do Analyze

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## Sintaxe SQL

```sql
URL_DECODE(<str>)
```

## Exemplos de SQL

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```

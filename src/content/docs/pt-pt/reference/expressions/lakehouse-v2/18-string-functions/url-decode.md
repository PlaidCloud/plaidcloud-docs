---
title: URL_DECODE (Lakehouse v2)
description: URL_DECODE — descodifica uma cadeia codificada para URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

Descodifica uma cadeia codificada para URL.

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

## Exemplos SQL

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```

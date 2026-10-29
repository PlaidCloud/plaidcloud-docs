---
title: URL_DECODE (Lakehouse v2)
description: URL_DECODE — dekoduje ciąg zakodowany jako URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

Dekoduje ciąg zakodowany jako URL.

## Składnia Analyze

```python
func.url_decode(<str>)
```

## Przykłady Analyze

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## Składnia SQL

```sql
URL_DECODE(<str>)
```

## Przykłady SQL

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```

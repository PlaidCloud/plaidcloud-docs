---
title: URL_ENCODE (Lakehouse v2)
description: URL_ENCODE — koduje ciąg do użycia w adresie URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-encode.md
---

Koduje ciąg do użycia w adresie URL.

## Składnia Analyze

```python
func.url_encode(<str>)
```

## Przykłady Analyze

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## Składnia SQL

```sql
URL_ENCODE(<str>)
```

## Przykłady SQL

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```

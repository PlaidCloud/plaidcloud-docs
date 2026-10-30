---
title: URL_ENCODE (Lakehouse v2)
description: URL_ENCODE — kodiert eine Zeichenfolge für die Verwendung in einer URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-encode.md
---

Kodiert eine Zeichenfolge für die Verwendung in einer URL.

## Analyze-Syntax

```python
func.url_encode(<str>)
```

## Analyze-Beispiele

```python
func.url_encode('hello world')

┌─────────────────┐
│ 'hello%20world'  │
└─────────────────┘
```

## SQL-Syntax

```sql
URL_ENCODE(<str>)
```

## SQL-Beispiele

```sql
SELECT URL_ENCODE('hello world');

┌───────────────┐
│ hello%20world  │
└───────────────┘
```

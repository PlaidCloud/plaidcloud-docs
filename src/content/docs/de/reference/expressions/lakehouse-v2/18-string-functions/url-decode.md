---
title: URL_DECODE (Lakehouse v2)
description: URL_DECODE — dekodiert eine URL-kodierte Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/url-decode.md
---

Dekodiert eine URL-kodierte Zeichenfolge.

## Analyze-Syntax

```python
func.url_decode(<str>)
```

## Analyze-Beispiele

```python
func.url_decode('hello%20world')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## SQL-Syntax

```sql
URL_DECODE(<str>)
```

## SQL-Beispiele

```sql
SELECT URL_DECODE('hello%20world');

┌─────────────┐
│ hello world  │
└─────────────┘
```

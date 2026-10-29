---
title: PARSE_URL (Lakehouse v2)
description: PARSE_URL — extrahiert einen angegebenen Teil aus einer URL-Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/parse-url.md
---

Extrahiert einen angegebenen Teil aus einer URL-Zeichenfolge.

## Analyze-Syntax

```python
func.parse_url(<url>, <part>)
```

## Analyze-Beispiele

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## SQL-Syntax

```sql
PARSE_URL(<url>, <part>)
```

## SQL-Beispiele

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```

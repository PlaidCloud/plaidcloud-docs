---
title: PARSE_URL (Lakehouse v2)
description: PARSE_URL — Extrae una parte especificada de una cadena de URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/parse-url.md
---

Extrae una parte especificada de una cadena de URL.

## Sintaxis de Analyze

```python
func.parse_url(<url>, <part>)
```

## Ejemplos de Analyze

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
PARSE_URL(<url>, <part>)
```

## Ejemplos de SQL

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```

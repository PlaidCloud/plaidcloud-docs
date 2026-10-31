---
title: PARSE_URL (Lakehouse v2)
description: PARSE_URL — extrait une partie donnée d'une chaîne d'URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/parse-url.md
---

Extrait une partie donnée d'une chaîne d'URL.

## Syntaxe Analyze

```python
func.parse_url(<url>, <part>)
```

## Exemples Analyze

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## Syntaxe SQL

```sql
PARSE_URL(<url>, <part>)
```

## Exemples SQL

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```

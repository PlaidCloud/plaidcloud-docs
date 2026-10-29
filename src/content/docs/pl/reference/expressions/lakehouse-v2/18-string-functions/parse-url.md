---
title: PARSE_URL (Lakehouse v2)
description: PARSE_URL — wyodrębnia wskazaną część z adresu URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/parse-url.md
---

Wyodrębnia wskazaną część z adresu URL.

## Składnia Analyze

```python
func.parse_url(<url>, <part>)
```

## Przykłady Analyze

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## Składnia SQL

```sql
PARSE_URL(<url>, <part>)
```

## Przykłady SQL

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```

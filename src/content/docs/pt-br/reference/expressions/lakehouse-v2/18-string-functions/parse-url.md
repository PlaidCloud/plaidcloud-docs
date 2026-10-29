---
title: PARSE_URL (Lakehouse v2)
description: PARSE_URL — extrai uma parte especificada de uma string de URL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/parse-url.md
---

Extrai uma parte especificada de uma string de URL.

## Sintaxe do Analyze

```python
func.parse_url(<url>, <part>)
```

## Exemplos do Analyze

```python
func.parse_url('https://example.com/path?q=1', 'HOST')

┌───────────────┐
│ 'example.com'  │
└───────────────┘
```

## Sintaxe SQL

```sql
PARSE_URL(<url>, <part>)
```

## Exemplos de SQL

```sql
SELECT PARSE_URL('https://example.com/path?q=1', 'HOST');

┌─────────────┐
│ example.com  │
└─────────────┘
```

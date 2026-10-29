---
title: REGEXP_SPLIT (Lakehouse v2)
description: REGEXP_SPLIT — dzieli ciąg według wzorca wyrażenia regularnego i zwraca tablicę podciągów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/regexp-split.md
---

Dzieli ciąg według wzorca wyrażenia regularnego i zwraca tablicę podciągów.

## Składnia Analyze

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Przykłady Analyze

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## Składnia SQL

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## Przykłady SQL

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

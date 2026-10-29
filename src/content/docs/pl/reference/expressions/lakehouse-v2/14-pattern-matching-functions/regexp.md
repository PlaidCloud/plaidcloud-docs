---
title: REGEXP (Lakehouse v2)
description: REGEXP — sprawdza, czy ciąg znaków pasuje do wzorca wyrażenia regularnego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp.md
---

Sprawdza, czy ciąg znaków pasuje do wzorca wyrażenia regularnego.

## Składnia Analyze

```python
func.regexp(<str> REGEXP <pattern>)
```

## Przykłady Analyze

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## Składnia SQL

```sql
REGEXP(<str> REGEXP <pattern>)
```

## Przykłady SQL

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```

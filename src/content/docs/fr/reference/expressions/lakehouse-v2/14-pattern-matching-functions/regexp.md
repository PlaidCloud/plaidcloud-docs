---
title: REGEXP (Lakehouse v2)
description: REGEXP — vérifie si une chaîne correspond à un motif d'expression régulière.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp.md
---

Vérifie si une chaîne correspond à un motif d'expression régulière.

## Syntaxe Analyze

```python
func.regexp(<str> REGEXP <pattern>)
```

## Exemples Analyze

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## Syntaxe SQL

```sql
REGEXP(<str> REGEXP <pattern>)
```

## Exemples SQL

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```

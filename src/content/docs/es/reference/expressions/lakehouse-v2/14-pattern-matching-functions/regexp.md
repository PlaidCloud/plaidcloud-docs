---
title: REGEXP (Lakehouse v2)
description: REGEXP — comprueba si una cadena coincide con un patrón de expresión regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp.md
---

Comprueba si una cadena coincide con un patrón de expresión regular.

## Sintaxis de Analyze

```python
func.regexp(<str> REGEXP <pattern>)
```

## Ejemplos de Analyze

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## Sintaxis de SQL

```sql
REGEXP(<str> REGEXP <pattern>)
```

## Ejemplos de SQL

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```

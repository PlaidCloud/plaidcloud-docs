---
title: REGEXP (Lakehouse v2)
description: REGEXP — verifica se uma cadeia de caracteres corresponde a um padrão de expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp.md
---

Verifica se uma cadeia de caracteres corresponde a um padrão de expressão regular.

## Sintaxe de Analyze

```python
func.regexp(<str> REGEXP <pattern>)
```

## Exemplos de Analyze

```python
get_column(table, 'email').regexp_match('^[a-z]+@')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## Sintaxe SQL

```sql
REGEXP(<str> REGEXP <pattern>)
```

## Exemplos SQL

```sql
SELECT email FROM users WHERE email REGEXP '^[a-z]+@[a-z]+\\.com$';

┌───────────────────┐
│ alice@example.com  │
└───────────────────┘
```

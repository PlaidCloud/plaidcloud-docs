---
title: IS_INTEGER (Lakehouse v1)
description: IS_INTEGER — Vérifie si la valeur JSON en entrée est un entier.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-integer.md
---

Vérifie si la valeur JSON en entrée est un entier.


## Syntaxe Analyze

```python
func.is_integer(<expr>)
```

## Exemples Analyze

```python

func.is_integer(func.parse_json('123')), func.is_integer(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_integer(func.parse_json('123'))  │ func.is_integer(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
IS_INTEGER( <expr> )
```

## Type de retour

Renvoie `true` si la valeur JSON en entrée est un entier, et `false` dans le cas contraire.

## Exemples SQL

```sql
SELECT
  IS_INTEGER(PARSE_JSON('123')),
  IS_INTEGER(PARSE_JSON('[1,2,3]'));

┌───────────────────────────────────────────────────────────────────┐
│ is_integer(parse_json('123')) │ is_integer(parse_json('[1,2,3]')) │
├───────────────────────────────┼───────────────────────────────────┤
│ true                          │ false                             │
└───────────────────────────────────────────────────────────────────┘
```

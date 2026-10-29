---
title: IS_BOOLEAN (Lakehouse v1)
description: IS_BOOLEAN — Vérifie si la valeur JSON en entrée est un booléen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-boolean.md
---

Vérifie si la valeur JSON en entrée est un booléen.

## Syntaxe Analyze

```python
func.is_boolean(<expr>)
```

## Exemples Analyze

```python

func.is_boolean(func.parse_json('true')), func.is_boolean(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_boolean(func.parse_json('true')) │ func.is_boolean(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
IS_BOOLEAN( <expr> )
```

## Type de retour

Renvoie `true` si la valeur JSON en entrée est un booléen, et `false` dans le cas contraire.

## Exemples SQL

```sql
SELECT
  IS_BOOLEAN(PARSE_JSON('true')),
  IS_BOOLEAN(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────────┐
│ is_boolean(parse_json('true')) │ is_boolean(parse_json('[1,2,3]')) │
├────────────────────────────────┼───────────────────────────────────┤
│ true                           │ false                             │
└────────────────────────────────────────────────────────────────────┘
```

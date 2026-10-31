---
title: CHECK_JSON (Lakehouse v1)
description: CHECK_JSON — Vérifie la validité d'un document JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/check-json.md
---

Vérifie la validité d'un document JSON.
Si la chaîne en entrée est un document JSON valide ou `NULL`, la sortie est `NULL`.
Si l'entrée ne peut pas être convertie en une valeur JSON valide, la chaîne de sortie contient le message d'erreur.

## Syntaxe Analyze

```python
func.check_json(<expr>)
```

## Exemples Analyze

```python
func.check_json('[1,2,3]');
┌────────────────────────────┐
│ func.check_json('[1,2,3]') │
├────────────────────────────┤
│ NULL                       │
└────────────────────────────┘
```

## Syntaxe SQL

```sql
CHECK_JSON( <expr> )
```

## Arguments

| Arguments | Description                       |
|-----------|-----------------------------------|
| `<expr>`  | Une expression de type chaîne     |

## Type de retour

Chaîne

## Exemples SQL

```sql
SELECT check_json('[1,2,3]');
┌───────────────────────┐
│ check_json('[1,2,3]') │
├───────────────────────┤
│ NULL                  │
└───────────────────────┘

SELECT check_json('{"key":"val"}');
┌─────────────────────────────┐
│ check_json('{"key":"val"}') │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘

SELECT check_json('{"key":');
┌──────────────────────────────────────────────┐
│ check_json('{"key":')                        │
├──────────────────────────────────────────────┤
│ EOF while parsing a value at line 1 column 7 │
└──────────────────────────────────────────────┘
```

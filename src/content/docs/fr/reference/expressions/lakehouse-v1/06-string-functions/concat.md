---
title: CONCAT (Lakehouse v1)
description: CONCAT renvoie la chaîne résultant de la concaténation des arguments.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

Renvoie la chaîne résultant de la concaténation des arguments. Accepte un ou plusieurs arguments. Si tous les arguments sont des chaînes non binaires, le résultat est une chaîne non binaire. Si les arguments incluent une chaîne binaire, le résultat est une chaîne binaire. Un argument numérique est converti en sa forme équivalente de chaîne non binaire.

## Syntaxe Analyze

```python
func.concat(<expr1>, ...)
```

## Exemples Analyze

```python
func.concat('data', 'bend')
┌─────────────────────────────┐
│ func.concat('data', 'bend') │
├─────────────────────────────┤
│ databend                    │
└─────────────────────────────┘
```

## Syntaxe SQL

```sql
CONCAT(<expr1>, ...)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr1>` | chaîne      |

## Type de retour

Une valeur de type de données `VARCHAR` ou `NULL`.

## Exemples SQL

```sql
SELECT CONCAT('data', 'bend');
┌────────────────────────┐
│ concat('data', 'bend') │
├────────────────────────┤
│ databend               │
└────────────────────────┘

SELECT CONCAT('data', NULL, 'bend');
┌──────────────────────────────┐
│ CONCAT('data', NULL, 'bend') │
├──────────────────────────────┤
│                         NULL │
└──────────────────────────────┘

SELECT CONCAT('14.3');
┌────────────────┐
│ concat('14.3') │
├────────────────┤
│ 14.3           │
└────────────────┘
```

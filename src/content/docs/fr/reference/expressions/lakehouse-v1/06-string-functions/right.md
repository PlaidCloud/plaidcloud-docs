---
title: RIGHT (Lakehouse v1)
description: RIGHT renvoie les len caractères les plus à droite de la chaîne str, ou NULL si l'un des arguments est NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

Renvoie les len caractères les plus à droite de la chaîne str, ou NULL si l'un des arguments est NULL.

## Syntaxe Analyze

```python
func.right(<str>, <len>)
```

## Exemples Analyze

```python
func.right('foobarbar', 4)
┌────────────────────────────┐
│ func.right('foobarbar', 4) │
├────────────────────────────┤
│ rbar                       │
└────────────────────────────┘
```

## Syntaxe SQL

```sql
RIGHT(<str>, <len>);
```

## Arguments

| Arguments | Description                                                         |
|-----------|---------------------------------------------------------------------|
| `<str>`   | La chaîne principale dont les caractères sont à extraire            |
| `<len>`   | Le nombre de caractères                                             |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```

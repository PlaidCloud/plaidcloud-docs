---
title: LEFT (Lakehouse v1)
description: LEFT renvoie les len caractères les plus à gauche de la chaîne str, ou NULL si l'un des arguments est NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

Renvoie les len caractères les plus à gauche de la chaîne str, ou NULL si l'un des arguments est NULL.

## Syntaxe Analyze

```python
func.left(<str>, <len>)
```

## Exemples Analyze

```python
func.left('foobarbar', 5)
┌───────────────────────────┐
│ func.left('foobarbar', 5) │
├───────────────────────────┤
│ fooba                     │
└───────────────────────────┘
```

## Syntaxe SQL

```sql
LEFT(<str>, <len>);
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
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```

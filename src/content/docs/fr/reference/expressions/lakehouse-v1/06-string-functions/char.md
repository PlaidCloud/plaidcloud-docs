---
title: CHAR (Lakehouse v1)
description: CHAR renvoie le caractère correspondant à chaque entier fourni.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

Renvoie le caractère correspondant à chaque entier fourni.

## Syntaxe Analyze

```python
func.char(N,...)
```

## Exemples Analyze

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## Syntaxe SQL

```sql
CHAR(N, ...)
```

## Arguments

| Arguments | Description      |
|-----------|------------------|
| N         | Colonne numérique |

## Type de retour

`BINARY`

## Exemples SQL

Cet exemple montre à la fois la valeur binaire renvoyée et sa représentation sous forme de chaîne.

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```

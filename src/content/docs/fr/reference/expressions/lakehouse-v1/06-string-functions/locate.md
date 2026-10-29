---
title: LOCATE (Lakehouse v1)
description: LOCATE renvoie la position de la première occurrence de la sous-chaîne substr dans la chaîne str, à partir d'une position facultative.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

La première syntaxe renvoie la position de la première occurrence de la sous-chaîne substr dans la chaîne str.
La seconde syntaxe renvoie la position de la première occurrence de la sous-chaîne substr dans la chaîne str, en commençant à la position pos.
Renvoie 0 si substr ne figure pas dans str. Renvoie NULL si l'un des arguments est NULL.

## Syntaxe Analyze

```python
func.locate(<substr>, <str>, <pos>)
```

## Exemples Analyze

```python
func.locate('bar', 'foobarbar')
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar') │
├────────────────────────────────────┤
│                                  5 │
└────────────────────────────────────┘
```

```python
func.locate('bar', 'foobarbar', 5)
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar', 5) │
├────────────────────────────────────┤
│                                  7 │
└────────────────────────────────────┘
```

## Syntaxe SQL

```sql
LOCATE(<substr>, <str>)
LOCATE(<substr>, <str>, <pos>)
```

## Arguments

| Arguments  | Description        |
|------------|--------------------|
| `<substr>` | La sous-chaîne.    |
| `<str>`    | La chaîne.         |
| `<pos>`    | La position.       |

## Type de retour

`BIGINT`

## Exemples SQL

```sql
SELECT LOCATE('bar', 'foobarbar')
┌────────────────────────────┐
│ LOCATE('bar', 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT LOCATE('xbar', 'foobar')
┌──────────────────────────┐
│ LOCATE('xbar', 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘

SELECT LOCATE('bar', 'foobarbar', 5)
┌───────────────────────────────┐
│ LOCATE('bar', 'foobarbar', 5) │
├───────────────────────────────┤
│                             7 │
└───────────────────────────────┘
```

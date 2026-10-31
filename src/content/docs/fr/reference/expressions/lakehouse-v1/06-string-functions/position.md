---
title: POSITION (Lakehouse v1)
description: POSITION(substr IN str) est un synonyme de LOCATE(substr,str).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str) est un synonyme de LOCATE(substr,str).
Renvoie la position de la première occurrence de la sous-chaîne substr dans la chaîne str.
Renvoie 0 si substr ne figure pas dans str. Renvoie NULL si l'un des arguments est NULL.

## Syntaxe Analyze

```python
func.position(<substr>, <str>)
```

## Exemples Analyze

```python
func.position('bar', 'foobarbar')
┌───────────────────────────────────┐
│ func.position('bar', 'foobarbar') │
├───────────────────────────────────┤
│                                 4 │
└───────────────────────────────────┘
```

## Syntaxe SQL

```sql
POSITION(<substr> IN <str>)
```

## Arguments

| Arguments  | Description        |
|------------|--------------------|
| `<substr>` | La sous-chaîne.    |
| `<str>`    | La chaîne.         |

## Type de retour

`BIGINT`

## Exemples SQL

```sql
SELECT POSITION('bar' IN 'foobarbar')
┌────────────────────────────┐
│ POSITION('bar' IN 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT POSITION('xbar' IN 'foobar')
┌──────────────────────────┐
│ POSITION('xbar' IN 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘
```

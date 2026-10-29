---
title: LOCATE (Lakehouse v2)
description: LOCATE — renvoie la position de la première occurrence d'une sous-chaîne dans une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

Renvoie la position de la première occurrence d'une sous-chaîne dans une chaîne.

## Syntaxe Analyze

```python
func.locate(<substr>, <str>[, <pos>])
```

## Exemples Analyze

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## Syntaxe SQL

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## Exemples SQL

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```

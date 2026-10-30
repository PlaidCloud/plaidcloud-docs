---
title: INSTR (Lakehouse v2)
description: INSTR — renvoie la position de la première occurrence d'une sous-chaîne dans une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/instr.md
---

Renvoie la position de la première occurrence d'une sous-chaîne dans une chaîne.

## Syntaxe Analyze

```python
func.instr(<str>, <substr>)
```

## Exemples Analyze

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## Syntaxe SQL

```sql
INSTR(<str>, <substr>)
```

## Exemples SQL

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```

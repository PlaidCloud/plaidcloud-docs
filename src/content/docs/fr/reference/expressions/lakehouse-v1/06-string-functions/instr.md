---
title: INSTR (Lakehouse v1)
description: INSTR renvoie la position de la première occurrence de la sous-chaîne substr dans la chaîne str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

Renvoie la position de la première occurrence de la sous-chaîne substr dans la chaîne str.
Équivaut à la forme à deux arguments de LOCATE(), sauf que l'ordre des arguments est inversé.

## Syntaxe Analyze

```python
func.instr(<str>, <substr>)
```

## Exemples Analyze

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## Syntaxe SQL

```sql
INSTR(<str>, <substr>)
```

## Arguments

| Arguments  | Description        |
|------------|--------------------|
| `<str>`    | La chaîne.         |
| `<substr>` | La sous-chaîne.    |

## Type de retour

`BIGINT`

## Exemples SQL

```sql
SELECT INSTR('foobarbar', 'bar');
┌───────────────────────────┐
│ INSTR('foobarbar', 'bar') │
├───────────────────────────┤
│                         4 │
└───────────────────────────┘

SELECT INSTR('xbar', 'foobar');
┌─────────────────────────┐
│ INSTR('xbar', 'foobar') │
├─────────────────────────┤
│                       0 │
└─────────────────────────┘
```

---
title: RPAD (Lakehouse v1)
description: RPAD renvoie la chaîne str complétée à droite par la chaîne padstr jusqu'à une longueur de len caractères.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rpad.md
---

Renvoie la chaîne str complétée à droite par la chaîne padstr jusqu'à une longueur de len caractères.
Si str est plus longue que len, la valeur renvoyée est tronquée à len caractères.

## Syntaxe Analyze

```python
func.rpad(<str>, <len>, <padstr>)
```

## Exemples Analyze

```python
func.rpad('hi',5,'?')
┌───────────────────────┐
│ func.rpad('hi',5,'?') │
├───────────────────────┤
│ hi???                 │
└───────────────────────┘

func.rpad('hi',1,'?')
┌───────────────────────┐
│ func.rpad('hi',1,'?') │
├───────────────────────┤
│ h                     │
└───────────────────────┘
```

## Syntaxe SQL

```sql
RPAD(<str>, <len>, <padstr>)
```

## Arguments

| Arguments  | Description                  |
|------------|------------------------------|
| `<str>`    | La chaîne.                   |
| `<len>`    | La longueur.                 |
| `<padstr>` | La chaîne de remplissage.    |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT RPAD('hi',5,'?');
┌────────────────────┐
│ RPAD('hi', 5, '?') │
├────────────────────┤
│ hi???              │
└────────────────────┘

SELECT RPAD('hi',1,'?');
┌────────────────────┐
│ RPAD('hi', 1, '?') │
├────────────────────┤
│ h                  │
└────────────────────┘
```

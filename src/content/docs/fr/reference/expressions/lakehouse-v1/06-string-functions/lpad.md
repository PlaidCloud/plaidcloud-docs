---
title: LPAD (Lakehouse v1)
description: LPAD renvoie la chaîne str complétée à gauche par la chaîne padstr jusqu'à une longueur de len caractères.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lpad.md
---

Renvoie la chaîne str complétée à gauche par la chaîne padstr jusqu'à une longueur de len caractères.
Si str est plus longue que len, la valeur renvoyée est tronquée à len caractères.

## Syntaxe Analyze

```python
func.lpad(<str>, <len>, <padstr>)
```

## Exemples Analyze

```python
func.lpad('hi',4,'??')
┌────────────────────────┐
│ func.lpad('hi',4,'??') │
├────────────────────────┤
│ ??hi                   │
└────────────────────────┘
```

```python
func.lpad('hi',1,'??')
┌────────────────────────┐
│ func.lpad('hi',1,'??') │
├────────────────────────┤
│ h                      │
└────────────────────────┘
```

## Syntaxe SQL

```sql
LPAD(<str>, <len>, <padstr>)
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
SELECT LPAD('hi',4,'??');
┌─────────────────────┐
│ LPAD('hi', 4, '??') │
├─────────────────────┤
│ ??hi                │
└─────────────────────┘

SELECT LPAD('hi',1,'??');
┌─────────────────────┐
│ LPAD('hi', 1, '??') │
├─────────────────────┤
│ h                   │
└─────────────────────┘
```

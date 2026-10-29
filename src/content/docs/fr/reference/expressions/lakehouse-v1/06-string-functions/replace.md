---
title: REPLACE (Lakehouse v1)
description: REPLACE renvoie la chaîne str dont toutes les occurrences de la chaîne from_str sont remplacées par la chaîne to_str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/replace.md
---

Renvoie la chaîne str dont toutes les occurrences de la chaîne from_str sont remplacées par la chaîne to_str.

## Syntaxe Analyze

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Exemples Analyze

```python
func.replace(<str>, <from_str>, <to_str>)
┌──────────────────────────────────────┐
│ func.replace('plaidCloud', 'p', 'P') │
├──────────────────────────────────────┤
│ PlaidCloud                           │
└──────────────────────────────────────┘
```

## Syntaxe SQL

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## Arguments

| Arguments    | Description                |
|--------------|----------------------------|
| `<str>`      | La chaîne.                 |
| `<from_str>` | La chaîne à remplacer.     |
| `<to_str>`   | La chaîne de remplacement. |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
┌─────────────────────────────────────┐
│ REPLACE('www.mysql.com', 'w', 'Ww') │
├─────────────────────────────────────┤
│ WwWwWw.mysql.com                    │
└─────────────────────────────────────┘
```

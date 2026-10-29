---
title: REVERSE (Lakehouse v1)
description: REVERSE renvoie la chaîne str dont l'ordre des caractères est inversé.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

Renvoie la chaîne str dont l'ordre des caractères est inversé.

## Syntaxe Analyze

```python
func.reverse(<str>)
```

## Exemples Analyze

```python
func.reverse('abc')
┌──────────────────────┐
│ func..reverse('abc') │
├──────────────────────┤
│ cba                  │
└──────────────────────┘
```

## Syntaxe SQL

```sql
REVERSE(<str>)
```

## Arguments

| Arguments | Description           |
|-----------|-----------------------|
| `<str>`   | La valeur de chaîne.  |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```

---
title: ARRAYS_ZIP (Lakehouse v1)
description: "ARRAYS_ZIP : fusionne plusieurs tableaux en un seul tableau de tuples."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

Fusionne plusieurs tableaux en un seul tableau de tuples.

## Syntaxe Analyze

```python
func.arrays_zip( <array1> [, ...] )
```

## Exemples Analyze

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## Arguments

| Arguments  | Description       |
|------------|-------------------|
| `<arrayN>` | Les ARRAY d'entrée. |

:::note
- La longueur de chaque tableau doit être identique.
:::

## Type de retour

Array(Tuple).

## Exemples SQL

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```

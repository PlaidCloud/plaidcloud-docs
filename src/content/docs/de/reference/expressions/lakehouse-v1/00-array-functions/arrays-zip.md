---
title: ARRAYS_ZIP (Lakehouse v1)
description: ARRAYS_ZIP – führt mehrere Arrays zu einem einzelnen Array aus Tupeln zusammen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

Führt mehrere Arrays zu einem einzelnen Array aus Tupeln zusammen.

## Analyze-Syntax

```python
func.arrays_zip( <array1> [, ...] )
```

## Analyze-Beispiele

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## Argumente

| Argumente  | Beschreibung          |
|------------|-----------------------|
| `<arrayN>` | Die Eingabe-ARRAYs.   |

:::note
- Alle Arrays müssen die gleiche Länge haben.
:::

## Rückgabetyp

Array(Tuple).

## SQL-Beispiele

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```

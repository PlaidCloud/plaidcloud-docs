---
title: ARRAYS_ZIP (Lakehouse v1)
description: ARRAYS_ZIP — combina varios arreglos en un único arreglo de tuplas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

Combina varios arreglos en un único arreglo de tuplas.

## Sintaxis de Analyze

```python
func.arrays_zip( <array1> [, ...] )
```

## Ejemplos de Analyze

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## Argumentos

| Argumentos | Descripción       |
|------------|-------------------|
| `<arrayN>` | Los ARRAY de entrada. |

:::note
- La longitud de cada arreglo debe ser la misma.
:::

## Tipo de retorno

Array(Tuple).

## Ejemplos de SQL

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```

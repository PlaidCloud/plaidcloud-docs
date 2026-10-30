---
title: ARRAY_SORT (Lakehouse v1)
description: ARRAY_SORT — ordena los elementos del arreglo en orden ascendente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-sort.md
---

Ordena los elementos del arreglo en orden ascendente.

## Sintaxis de Analyze

```sql
func.array_sort( <array>[, <order>, <nullposition>] )
```

| Parámetro    | Predeterminado | Descripción                                                                                                                                    |
|--------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC            | Especifica el orden de clasificación: ascendente (ASC) o descendente (DESC).                                                                   |
| nullposition | NULLS FIRST    | Determina la posición de los valores NULL en el resultado ordenado: al principio (NULLS FIRST) o al final (NULLS LAST) de la salida. |

## Ejemplos de Analyze

```sql
func.array_sort([1, 4, 3, 2])

┌────────────────────────────────┐
│ func.array_sort([1, 4, 3, 2])  │
├────────────────────────────────┤
│ [1,2,3,4]                      │
└────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_SORT( <array>[, <order>, <nullposition>] )
```

| Parámetro    | Predeterminado | Descripción                                                                                                                                    |
|--------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC            | Especifica el orden de clasificación: ascendente (ASC) o descendente (DESC).                                                                   |
| nullposition | NULLS FIRST    | Determina la posición de los valores NULL en el resultado ordenado: al principio (NULLS FIRST) o al final (NULLS LAST) de la salida. |

## Ejemplos de SQL

```sql
SELECT ARRAY_SORT([1, 4, 3, 2]);

┌──────────────────────────┐
│ array_sort([1, 4, 3, 2]) │
├──────────────────────────┤
│ [1,2,3,4]                │
└──────────────────────────┘
```

---
title: ARRAY_SORT (Lakehouse v1)
description: ARRAY_SORT — ordena os elementos da matriz por ordem ascendente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-sort.md
---

Ordena os elementos da matriz por ordem ascendente.

## Sintaxe do Analyze

```sql
func.array_sort( <array>[, <order>, <nullposition>] )
```

| Parâmetro | Valor predefinido | Descrição |
|---|---|---|
| order | ASC | Especifica a ordem de ordenação: ascendente (ASC) ou descendente (DESC). |
| nullposition | NULLS FIRST | Determina a posição dos valores NULL no resultado da ordenação: no início (NULLS FIRST) ou no fim (NULLS LAST) da saída ordenada. |

## Exemplos do Analyze

```sql
func.array_sort([1, 4, 3, 2])

┌────────────────────────────────┐
│ func.array_sort([1, 4, 3, 2])  │
├────────────────────────────────┤
│ [1,2,3,4]                      │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_SORT( <array>[, <order>, <nullposition>] )
```

| Parâmetro | Valor predefinido | Descrição |
|---|---|---|
| order | ASC | Especifica a ordem de ordenação: ascendente (ASC) ou descendente (DESC). |
| nullposition | NULLS FIRST | Determina a posição dos valores NULL no resultado da ordenação: no início (NULLS FIRST) ou no fim (NULLS LAST) da saída ordenada. |

## Exemplos SQL

```sql
SELECT ARRAY_SORT([1, 4, 3, 2]);

┌──────────────────────────┐
│ array_sort([1, 4, 3, 2]) │
├──────────────────────────┤
│ [1,2,3,4]                │
└──────────────────────────┘
```

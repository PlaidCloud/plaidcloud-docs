---
title: ARRAYS_ZIP (Lakehouse v1)
description: ARRAYS_ZIP — combina várias matrizes numa única matriz de tuplos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

Combina várias matrizes numa única matriz de tuplos.

## Sintaxe do Analyze

```python
func.arrays_zip( <array1> [, ...] )
```

## Exemplos do Analyze

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## Argumentos

| Argumentos | Descrição |
|---|---|
| `<arrayN>` | As matrizes (ARRAY) de entrada. |

:::note
- O comprimento de cada matriz tem de ser o mesmo.
:::

## Tipo de retorno

Array(Tuple).

## Exemplos SQL

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```

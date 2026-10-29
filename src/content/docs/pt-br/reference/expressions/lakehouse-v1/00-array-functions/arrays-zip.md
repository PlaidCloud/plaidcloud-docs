---
title: ARRAYS_ZIP (Lakehouse v1)
description: ARRAYS_ZIP mescla vários arrays em uma única tupla de array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

Mescla vários arrays em uma única tupla de array.

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

| Argumentos | Descrição                |
|------------|--------------------------|
| `<arrayN>` | Os ARRAYs de entrada.    |

:::note
- O comprimento de cada array deve ser o mesmo.
:::

## Tipo de Retorno

Array(Tuple).

## Exemplos de SQL

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```

---
title: ARRAY_FLATTEN (Lakehouse v1)
description: ARRAY_FLATTEN — aplana matrizes aninhadas, convertendo-as numa matriz de um só nível.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-flatten.md
---

Aplana matrizes aninhadas, convertendo-as numa matriz de um só nível.

## Sintaxe do Analyze

```python
func.array_flatten( <array> )
```

## Exemplos do Analyze

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_FLATTEN( <array> )
```

## Exemplos SQL

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```

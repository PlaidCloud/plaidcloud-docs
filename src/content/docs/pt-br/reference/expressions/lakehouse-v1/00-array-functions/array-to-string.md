---
title: ARRAY_TO_STRING (Lakehouse v1)
description: ARRAY_TO_STRING concatena os elementos de um array em uma única string, usando um separador especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-to-string.md
---

Concatena os elementos de um array em uma única string, usando um separador especificado.

## Sintaxe do Analyze

```python
func.array_to_string( <array>, '<separator>' )
```

## Exemplos do Analyze

```python
func.array_to_string(['apple', 'banana', 'cherry'], ', ') 

┌────────────────────────────────────────────────────────────┐
│ func.array_to_string(['apple', 'banana', 'cherry'], ', ')  │
├────────────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                      │
└────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## Exemplos de SQL

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```

---
title: ARRAY_TO_STRING (Lakehouse v1)
description: ARRAY_TO_STRING — concatena los elementos de un arreglo en una sola cadena mediante un separador especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-to-string.md
---

Concatena los elementos de un arreglo en una sola cadena mediante un separador especificado.

## Sintaxis de Analyze

```python
func.array_to_string( <array>, '<separator>' )
```

## Ejemplos de Analyze

```python
func.array_to_string(['apple', 'banana', 'cherry'], ', ') 

┌────────────────────────────────────────────────────────────┐
│ func.array_to_string(['apple', 'banana', 'cherry'], ', ')  │
├────────────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                      │
└────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```

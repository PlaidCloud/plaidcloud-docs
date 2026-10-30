---
title: CONTAINS (Lakehouse v1)
description: CONTAINS — comprueba si el arreglo contiene un elemento específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/contains.md
---

Comprueba si el arreglo contiene un elemento específico.


## Sintaxis de Analyze

```python
func.contains( <array>, <element> )
```

## Ejemplos de Analyze

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## Sintaxis de SQL

```sql
CONTAINS( <array>, <element> )
```

## Alias

- [ARRAY_CONTAINS](../array-contains)

## Ejemplos de SQL

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```

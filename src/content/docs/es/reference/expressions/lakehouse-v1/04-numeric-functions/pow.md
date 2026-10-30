---
title: POW (Lakehouse v1)
description: POW — devuelve el valor de x elevado a la potencia y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pow.md
---

Devuelve el valor de `x` elevado a la potencia `y`. 

## Sintaxis de Analyze

```python
func.pow( <x, y> )
```

## Ejemplos de Analyze

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## Sintaxis de SQL

```sql
POW( <x, y> )
```

## Alias

- [POWER](../power)

## Ejemplos de SQL

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```

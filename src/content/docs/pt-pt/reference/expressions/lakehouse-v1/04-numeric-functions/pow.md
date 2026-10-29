---
title: POW (Lakehouse v1)
description: POW — devolve o valor de x elevado à potência de y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pow.md
---

Devolve o valor de `x` elevado à potência de `y`. 

## Sintaxe do Analyze

```python
func.pow( <x, y> )
```

## Exemplos do Analyze

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## Sintaxe SQL

```sql
POW( <x, y> )
```

## Aliases

- [POWER](../power)

## Exemplos SQL

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```

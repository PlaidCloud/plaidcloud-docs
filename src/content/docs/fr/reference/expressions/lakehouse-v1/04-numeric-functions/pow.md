---
title: POW (Lakehouse v1)
description: POW — renvoie la valeur de x élevée à la puissance y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pow.md
---

Renvoie la valeur de `x` élevée à la puissance `y`. 

## Syntaxe Analyze

```python
func.pow( <x, y> )
```

## Exemples Analyze

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## Syntaxe SQL

```sql
POW( <x, y> )
```

## Alias

- [POWER](../power)

## Exemples SQL

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```

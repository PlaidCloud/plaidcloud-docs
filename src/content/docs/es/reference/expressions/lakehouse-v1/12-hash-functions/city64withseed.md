---
title: CITY64WITHSEED (Lakehouse v1)
description: CITY64WITHSEED calcula un hash City64WithSeed de 64 bits para una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/city64withseed.md
---

Calcula un hash City64WithSeed de 64 bits para una cadena.

## Sintaxis de Analyze

```python
func.city64withseed(<expr1>, <expr2>)
```

## Ejemplos de Analyze

```python
func.city64withseed('1234567890', 12)

┌───────────────────────────────────────┐
│ func.city64withseed('1234567890', 12) │
├───────────────────────────────────────┤
│                  10660895976650300430 │
└───────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## Ejemplos de SQL

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```

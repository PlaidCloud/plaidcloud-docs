---
title: CITY64WITHSEED (Lakehouse v1)
description: CITY64WITHSEED — calcula um hash City64WithSeed de 64 bits para uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/city64withseed.md
---

Calcula um hash City64WithSeed de 64 bits para uma string.

## Sintaxe no Analyze

```python
func.city64withseed(<expr1>, <expr2>)
```

## Exemplos no Analyze

```python
func.city64withseed('1234567890', 12)

┌───────────────────────────────────────┐
│ func.city64withseed('1234567890', 12) │
├───────────────────────────────────────┤
│                  10660895976650300430 │
└───────────────────────────────────────┘
```

## Sintaxe SQL

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## Exemplos de SQL

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```

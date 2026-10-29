---
title: DEGREES (Lakehouse v1)
description: DEGREES — retorna o argumento x convertido de radianos para graus, em que x é dado em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/degrees.md
---

Retorna o argumento `x` convertido de radianos para graus, em que `x` é dado em radianos.

## Sintaxe do Analyze

```python
func.degrees( <x> )
```

## Exemplos do Analyze

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
DEGREES( <x> )
```

## Exemplos de SQL

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```

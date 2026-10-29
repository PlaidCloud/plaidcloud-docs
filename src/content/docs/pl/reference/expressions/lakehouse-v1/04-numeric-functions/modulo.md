---
title: MODULO (Lakehouse v1)
description: MODULO — zwraca resztę z dzielenia x przez y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/modulo.md
---

Zwraca resztę z dzielenia `x` przez `y`. Jeśli `y` wynosi 0, zwraca błąd.

## Składnia Analyze

```python
func.modulo( <x>, <y> )
```

## Przykłady Analyze

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## Składnia SQL

```sql
MODULO( <x>, <y> )
```

## Aliasy

- [MOD](../mod)

## Przykłady SQL

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```

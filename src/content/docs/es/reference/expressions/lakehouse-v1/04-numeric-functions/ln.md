---
title: LN (Lakehouse v1)
description: LN — devuelve el logaritmo natural de x; es decir, el logaritmo en base e de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

Devuelve el logaritmo natural de `x`; es decir, el logaritmo en base e de `x`. Si x es menor o igual que 0.0E0, la función devuelve NULL.

## Sintaxis de Analyze

```python
func.ln( <x> )
```

## Ejemplos de Analyze

```python
func.ln(2)

┌────────────────────┐
│     func.ln(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
LN( <x> )
```

## Ejemplos de SQL

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

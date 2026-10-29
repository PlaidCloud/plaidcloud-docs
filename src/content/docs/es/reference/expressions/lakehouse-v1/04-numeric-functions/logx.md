---
title: LOG(x) (Lakehouse v1)
description: LOG(x) — devuelve el logaritmo natural de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logx.md
---

Devuelve el logaritmo natural de `x`. Si x es menor o igual que 0.0E0, la función devuelve NULL.

## Sintaxis de Analyze

```python
 func.log( <x> )
```

## Ejemplos de Analyze

```python
 func.log(2)

┌────────────────────┐
│    func.log(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
LOG( <x> )
```

## Ejemplos de SQL

```sql
SELECT LOG(2);

┌────────────────────┐
│       log(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

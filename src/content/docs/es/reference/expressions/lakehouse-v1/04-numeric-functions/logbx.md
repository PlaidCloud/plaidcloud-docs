---
title: "LOG(b, x) (Lakehouse v1)"
description: LOG(b, x) — devuelve el logaritmo en base b de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

Devuelve el logaritmo en base b de `x`. Si `x` es menor o igual que 0.0E0, la función devuelve NULL.

## Sintaxis de Analyze

```python
func.log( <b, x> )
```

## Ejemplos de Analyze

```python
func.log(2, 65536)

┌────────────────────┐
│ func.log(2, 65536) │
├────────────────────┤
│                 16 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
LOG( <b, x> )
```

## Ejemplos de SQL

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```

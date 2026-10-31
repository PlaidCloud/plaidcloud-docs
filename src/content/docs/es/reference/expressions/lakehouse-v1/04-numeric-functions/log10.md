---
title: LOG10 (Lakehouse v1)
description: LOG10 — devuelve el logaritmo en base 10 de x. Referencia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

Devuelve el logaritmo en base 10 de `x`. Si `x` es menor o igual que 0.0E0, la función devuelve NULL.


## Sintaxis de Analyze

```python
func.log10( <x> )
```

## Ejemplos de Analyze

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## Sintaxis de SQL

```sql
LOG10( <x> )
```

## Ejemplos de SQL

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```

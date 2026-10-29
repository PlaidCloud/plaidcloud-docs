---
title: TO_QUARTER (Lakehouse v1)
description: TO_QUARTER — obtiene el trimestre (1, 2, 3 o 4) de una fecha o marca de tiempo dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-quarter.md
---

Obtiene el trimestre (1, 2, 3 o 4) de una fecha o marca de tiempo dada.

## Sintaxis de Analyze

```python
func.to_quarter(<expr>)
```

## Ejemplos de Analyze

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_QUARTER( <date_or_time_expr> )
```

## Alias

- [QUARTER](../quarter)

## Tipo de valor devuelto

Entero.

## Ejemplos de SQL

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```

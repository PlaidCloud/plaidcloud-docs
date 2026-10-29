---
title: TO_MILLENNIA (Lakehouse v1)
description: TO_MILLENNIA — convierte un número determinado de milenios en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-millennia.md
---

Convierte un número determinado de milenios en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_millennia(<millennia>)
```

## Ejemplos de Analyze

```python
func.to_millennia(2)
┌──────────────────────────────────────────────────────┐
│ func.to_millennia(2)                                 │
├──────────────────────────────────────────────────────┤
│ 2000 years                                            │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_MILLENNIA(<millennia>)
```

## Tipo de retorno

Interval (representado en años).

## Ejemplos de SQL

```sql
SELECT TO_MILLENNIA(2), TO_MILLENNIA(0), TO_MILLENNIA((- 2));

┌───────────────────────────────────────────────────────┐
│ to_millennia(2) │ to_millennia(0) │ to_millennia(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 2000 years      │ 00:00:00        │ -2000 years       │
└───────────────────────────────────────────────────────┘
```

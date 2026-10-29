---
title: TO_MICROSECONDS (Lakehouse v1)
description: TO_MICROSECONDS — convierte un número determinado de microsegundos en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-microseconds.md
---

Convierte un número determinado de microsegundos en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_microseconds(<microseconds>)
```

## Ejemplos de Analyze

```python
func.to_microseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_microseconds(2)                              │
├──────────────────────────────────────────────────────┤
│ 0:00:00.000002                                       │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_MICROSECONDS(<microseconds>)
```

## Tipo de retorno

Interval (con el formato `hh:mm:ss.sssssss`).

## Ejemplos de SQL

```sql
SELECT TO_MICROSECONDS(2), TO_MICROSECONDS(0), TO_MICROSECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_microseconds(2) │ to_microseconds(0) │ to_microseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.000002     │ 00:00:00           │ -0:00:00.000002      │
└────────────────────────────────────────────────────────────────┘
```

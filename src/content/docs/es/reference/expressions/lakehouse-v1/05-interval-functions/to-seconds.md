---
title: TO_SECONDS (Lakehouse v1)
description: TO_SECONDS — convierte un número determinado de segundos en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-seconds.md
---

Convierte un número determinado de segundos en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_seconds(<seconds>)
```

## Ejemplos de Analyze

```python
func.to_seconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_seconds(2)                                   │
├──────────────────────────────────────────────────────┤
│ 0:00:02                                              │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_SECONDS(<seconds>)
```

## Alias

- [EPOCH](../epoch)

## Tipo de retorno

Interval (con el formato `hh:mm:ss`).

## Ejemplos de SQL

```sql
SELECT TO_SECONDS(2), TO_SECONDS(0), TO_SECONDS((- 2));

┌─────────────────────────────────────────────────┐
│ to_seconds(2) │ to_seconds(0) │ to_seconds(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 0:00:02       │ 00:00:00      │ -0:00:02        │
└─────────────────────────────────────────────────┘
```

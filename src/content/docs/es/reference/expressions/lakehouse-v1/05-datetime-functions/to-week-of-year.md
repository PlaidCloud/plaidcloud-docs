---
title: TO_WEEK_OF_YEAR (Lakehouse v1)
description: TO_WEEK_OF_YEAR — calcula el número de semana dentro de un año para una fecha determinada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-week-of-year.md
---

Calcula el número de semana dentro de un año para una fecha determinada.

La numeración de semanas ISO funciona así: el 4 de enero siempre se considera parte de la primera semana. Si el 1 de enero es jueves, la semana que va del lunes 29 de diciembre al domingo 4 de enero es la semana ISO 1. Si el 1 de enero cae en viernes, la semana que va del lunes 4 de enero al domingo 10 de enero es la semana ISO 1.

## Sintaxis de Analyze

```python
func.to_week_of_year(<expr>)
```

## Ejemplos de Analyze

```python
func.now(), func.to_week_of_year(func.now()), func.week(func.now()), func.weekofyear(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_week_of_year(func.now()) │ func.week(func.now()) │ func.weekofyear(func.now()) │
├────────────────────────────┼──────────────────────────────────┼───────────────────────┼─────────────────────────────┤
│ 2024-03-14 23:30:04.011624 │                               11 │                    11 │                          11 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_WEEK_OF_YEAR(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Alias

- [WEEK](../week)
- [WEEKOFYEAR](../weekofyear)

## Tipo de retorno

Devuelve un entero que representa el número de semana dentro de un año, con una numeración de 1 a 53.

## Ejemplos de SQL

```sql
SELECT NOW(), TO_WEEK_OF_YEAR(NOW()), WEEK(NOW()), WEEKOFYEAR(NOW());

┌───────────────────────────────────────────────────────────────────────────────────────┐
│            now()           │ to_week_of_year(now()) │ week(now()) │ weekofyear(now()) │
├────────────────────────────┼────────────────────────┼─────────────┼───────────────────┤
│ 2024-03-14 23:30:04.011624 │                     11 │          11 │                11 │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

---
title: TO_START_OF_YEAR (Lakehouse v1)
description: TO_START_OF_YEAR — devuelve el primer día del año para una fecha o una fecha con hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-year.md
---

Devuelve el primer día del año para una fecha o una fecha con hora (marca de tiempo/datetime).

## Sintaxis de Analyze

```python
func.to_start_of_year(<expr>)
```

## Ejemplos de Analyze

```python
func.to_start_of_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_year('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-01-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_START_OF_YEAR(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Tipo de retorno

`DATE`, devuelve la fecha en formato “YYYY-MM-DD”.

## Ejemplos de SQL

```sql
SELECT
  to_start_of_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_year('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-01-01                                     │
└────────────────────────────────────────────────┘
```

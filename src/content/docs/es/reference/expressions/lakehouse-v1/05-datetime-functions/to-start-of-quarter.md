---
title: TO_START_OF_QUARTER (Lakehouse v1)
description: TO_START_OF_QUARTER — redondea hacia abajo una fecha o una fecha con hora (marca de tiempo) al primer día del trimestre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-quarter.md
---

Redondea hacia abajo una fecha o una fecha con hora (marca de tiempo/datetime) al primer día del trimestre.
El primer día del trimestre es el 1 de enero, el 1 de abril, el 1 de julio o el 1 de octubre.
Devuelve la fecha.

## Sintaxis de Analyze

```python
func.to_start_of_quarter(<expr>)
```

## Ejemplos de Analyze

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_START_OF_QUARTER(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`   | fecha/marca de tiempo |

## Tipo de retorno

`DATE`, devuelve la fecha en formato “YYYY-MM-DD”.

## Ejemplos de SQL

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```

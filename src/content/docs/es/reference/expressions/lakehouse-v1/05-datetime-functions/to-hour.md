---
title: TO_HOUR (Lakehouse v1)
description: TO_HOUR — convierte una fecha con hora (marca de tiempo/datetime) en un número UInt8 que contiene la hora en formato de 24 horas (0-23).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-hour.md
---

Convierte una fecha con hora (marca de tiempo/datetime) en un número UInt8 que contiene la hora en formato de 24 horas (0-23).
Esta función supone que, si los relojes se adelantan, es una hora y ocurre a las 2 a. m., y que, si se atrasan, es una hora y ocurre a las 3 a. m. (lo cual no siempre es cierto; incluso en Moscú los relojes se cambiaron dos veces en momentos distintos).


## Sintaxis de Analyze

```python
func.to_hour(<expr>)
```

## Ejemplos de Analyze

```python
func.to_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_hour('2023-11-12 09:38:18.165575')         │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  9 │
└────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_HOUR(<expr>)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<expr>`  | marca de tiempo |

## Tipo de valor devuelto

`TINYINT`

## Ejemplos de SQL

```sql
SELECT
    to_hour('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────┐
│ to_hour('2023-11-12 09:38:18.165575') │
│                 UInt8                 │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘
```

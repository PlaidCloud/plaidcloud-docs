---
title: TO_MINUTE (Lakehouse v1)
description: TO_MINUTE — convierte una fecha con hora (marca de tiempo/datetime) en un número UInt8 que contiene el minuto de la hora (0-59).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-minute.md
---

Convierte una fecha con hora (marca de tiempo/datetime) en un número UInt8 que contiene el minuto de la hora (0-59).


## Sintaxis de Analyze

```python
func.to_minute(<expr>)
```

## Ejemplos de Analyze

```python
func.to_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_minute('2023-11-12 09:38:18.165575')       │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                 38 │
└────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_MINUTE(<expr>)
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
    to_minute('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_minute('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      38 │
└─────────────────────────────────────────┘
```

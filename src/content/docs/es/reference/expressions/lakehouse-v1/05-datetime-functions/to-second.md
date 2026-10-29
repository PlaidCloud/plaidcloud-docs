---
title: TO_SECOND (Lakehouse v1)
description: TO_SECOND — convierte una fecha con hora (marca de tiempo/datetime) en un número UInt8 que contiene el segundo dentro del minuto (0-59).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-second.md
---

Convierte una fecha con hora (marca de tiempo/datetime) en un número UInt8 que contiene el segundo dentro del minuto (0-59).

## Sintaxis de Analyze

```python
func.to_second(<expr>)
```

## Ejemplos de Analyze

```python
func.to_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_second('2023-11-12 09:38:18.165575') │
│                   UInt8                      │
├──────────────────────────────────────────────┤
│                                           18 │
└──────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_SECOND(<expr>)
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
    to_second('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_second('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      18 │
└─────────────────────────────────────────┘
```

---
title: TO_YYYYMMDDHHMMSS (Lakehouse v1)
description: TO_YYYYMMDDHHMMSS — convierte una fecha o una fecha con hora (marca de tiempo) en un número UInt64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhhmmss.md
---

Convierte una fecha o una fecha con hora (marca de tiempo/datetime) en un número UInt64 que contiene el año, el mes, el día, la hora, los minutos y los segundos (YYYY * 10000000000 + MM * 100000000 + DD * 1000000 + hh * 10000 + mm * 100 + ss).

## Sintaxis de Analyze

```python
func.to_yyyymmddhhmmss(<expr>)
```

## Ejemplos de Analyze

```python
func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────────┐
│ func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                   UInt64                             │
├──────────────────────────────────────────────────────┤
│                                       20231112092818 │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_YYYYMMDDHHMMSS(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Tipo de retorno

`BIGINT`, devuelve el valor en formato `YYYYMMDDhhmmss`.

## Ejemplos de SQL

```sql
SELECT
  to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                      UInt64                     │
├─────────────────────────────────────────────────┤
│                                  20231112092818 │
└─────────────────────────────────────────────────┘
```

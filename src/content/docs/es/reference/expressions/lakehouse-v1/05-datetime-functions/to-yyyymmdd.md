---
title: TO_YYYYMMDD (Lakehouse v1)
description: TO_YYYYMMDD — convierte una fecha o una fecha con hora (marca de tiempo) en un número UInt32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmdd.md
---

Convierte una fecha o una fecha con hora (marca de tiempo/datetime) en un número UInt32 que contiene el año, el mes y el día (YYYY * 10000 + MM * 100 + DD).

## Sintaxis de Analyze

```python
func.to_yyyymmdd(<expr>)
```

## Ejemplos de Analyze

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_YYYYMMDD(<expr>)
```

## Argumentos

| Argumentos | Descripción   |
|-----------|---------------|
| `<expr>`  | fecha/datetime |

## Tipo de retorno

`INT`, devuelve el valor en formato `YYYYMMDD`.

## Ejemplos de SQL

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```

---
title: TO_YYYYMM (Lakehouse v1)
description: TO_YYYYMM — convierte una fecha o una fecha con hora (marca de tiempo) en un número UInt32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymm.md
---

Convierte una fecha o una fecha con hora (marca de tiempo/datetime) en un número UInt32 que contiene el año y el número del mes.

## Sintaxis de Analyze

```python
func.to_yyyymm(<expr>)
```

## Ejemplos de Analyze

```python
func.to_yyyymm('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_yyyymm('2023-11-12 09:38:18.165575') │
│                   UInt32                     │
├──────────────────────────────────────────────┤
│                                       202311 │
└──────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_YYYYMM(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Tipo de retorno

`INT`, devuelve el valor en formato `YYYYMM`.

## Ejemplos de SQL

```sql
SELECT
  to_yyyymm('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_yyyymm('2023-11-12 09:38:18.165575') │
│                  UInt32                 │
├─────────────────────────────────────────┤
│                                  202311 │
└─────────────────────────────────────────┘
```

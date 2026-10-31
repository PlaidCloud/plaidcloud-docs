---
title: TO_MONTH (Lakehouse v1)
description: TO_MONTH — convierte una fecha, o fecha con hora (marca de tiempo/datetime), en un número UInt8 que contiene el mes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-month.md
---

Convierte una fecha, o fecha con hora (marca de tiempo/datetime), en un número UInt8 que contiene el número del mes (1-12).

## Sintaxis de Analyze

```python
func.to_month(<expr>)
```

## Ejemplos de Analyze

```python
func.now(), func.to_month(func.now()), func.month(func.now())

┌─────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_month(func.now()) │ func.month(func.now()) │
├────────────────────────────┼───────────────────────────┼────────────────────────┤
│ 2024-03-14 23:34:02.161291 │                         3 │                      3 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_MONTH(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Alias

- [MONTH](../month)

## Tipo de valor devuelto

 `TINYINT`

## Ejemplos de SQL

```sql
SELECT NOW(), TO_MONTH(NOW()), MONTH(NOW());

┌─────────────────────────────────────────────────────────────┐
│            now()           │ to_month(now()) │ month(now()) │
├────────────────────────────┼─────────────────┼──────────────┤
│ 2024-03-14 23:34:02.161291 │               3 │            3 │
└─────────────────────────────────────────────────────────────┘
```

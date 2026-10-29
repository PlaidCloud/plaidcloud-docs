---
title: TO_UNIX_TIMESTAMP (Lakehouse v1)
description: TO_UNIX_TIMESTAMP — convierte una marca de tiempo en formato de fecha y hora al formato de marca de tiempo Unix.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-unix-timestamp.md
---

Convierte una marca de tiempo en formato de fecha y hora al formato de marca de tiempo Unix. Una marca de tiempo Unix representa el número de segundos transcurridos desde el 1 de enero de 1970 a las 00:00:00 UTC.

## Sintaxis de Analyze

```python
func.to_unix_timestamp(<expr>)
```

## Ejemplos de Analyze

```python
func.to_unix_timestamp('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_unix_timestamp('2023-11-12 09:38:18.165575')           │
│                          UInt32                                │
├────────────────────────────────────────────────────────────────┤
│                                                     1699781898 │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_UNIX_TIMESTAMP(<expr>)
```

## Argumentos

| Argumentos   | Descripción         |
| ----------- | ------------------- |
| `<expr>`    | Marca de tiempo           |

Para obtener más información sobre el tipo de datos de marca de tiempo, consulte Date & Time.

## Tipo de retorno

`BIGINT`

## Ejemplos de SQL

```sql
SELECT
  to_unix_timestamp('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_unix_timestamp('2023-11-12 09:38:18.165575') │
│                      UInt32                     │
├─────────────────────────────────────────────────┤
│                                      1699781898 │
└─────────────────────────────────────────────────┘
```

---
title: TIMESTAMP_DIFF (Lakehouse v1)
description: TIMESTAMP_DIFF — calcula la diferencia entre dos marcas de tiempo y devuelve el resultado como un INTERVAL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timestamp-diff.md
---

Calcula la diferencia entre dos marcas de tiempo y devuelve el resultado como un INTERVAL.

## Sintaxis de Analyze

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Ejemplos de Analyze

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## Tipo de valor devuelto

INTERVAL (con el formato `hours:minutes:seconds`).

## Ejemplos de SQL

Este ejemplo muestra que la diferencia de tiempo entre el 1 de febrero de 2025 y el 1 de enero de 2025 es de 744 horas, que corresponden a 31 días:

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```

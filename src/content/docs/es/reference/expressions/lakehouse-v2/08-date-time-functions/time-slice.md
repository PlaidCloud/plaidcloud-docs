---
title: TIME_SLICE (Lakehouse v2)
description: TIME_SLICE — convierte una hora dada al inicio o al final de un intervalo de tiempo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-slice.md
---

Convierte una hora dada al inicio o al final de un intervalo de tiempo.

## Sintaxis de Analyze

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Ejemplos de Analyze

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Ejemplos de SQL

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

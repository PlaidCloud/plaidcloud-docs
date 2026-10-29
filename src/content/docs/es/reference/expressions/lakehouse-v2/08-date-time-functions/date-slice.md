---
title: DATE_SLICE (Lakehouse v2)
description: "Use la función de fecha y hora DATE_SLICE en PlaidCloud Lakehouse. Convierte una hora determinada en el inicio o el final de un intervalo de tiempo según el período especificado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-slice.md
---

Convierte una hora determinada en el inicio o el final de un intervalo de tiempo según el período especificado.

## Sintaxis de Analyze

```python
func.date_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Ejemplos de Analyze

```python
func.date_slice('2024-06-15 14:35:00', text('INTERVAL 1 HOUR'))

┌───────────────────────┐
│ '2024-06-15 14:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
DATE_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Ejemplos de SQL

```sql
SELECT DATE_SLICE('2024-06-15 14:35:00', INTERVAL 1 HOUR);

┌─────────────────────┐
│ 2024-06-15 14:00:00  │
└─────────────────────┘
```

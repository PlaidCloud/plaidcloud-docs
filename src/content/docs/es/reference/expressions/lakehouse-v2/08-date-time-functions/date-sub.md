---
title: DATE_SUB (Lakehouse v2)
description: DATE_SUB — resta un intervalo de tiempo específico a una fecha o a un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-sub.md
---

Resta un intervalo de tiempo específico a una fecha o a un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Ejemplos de Analyze

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## Ejemplos de SQL

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```

---
title: DATE_ADD (Lakehouse v2)
description: DATE_ADD — suma un intervalo de tiempo específico a una fecha o a un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-add.md
---

Suma un intervalo de tiempo específico a una fecha o a un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.date_add(<date>, INTERVAL <n> <unit>)
```

## Ejemplos de Analyze

```python
func.date_add('2024-01-01', text('INTERVAL 30 DAY'))

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
DATE_ADD(<date>, INTERVAL <n> <unit>)
```

## Ejemplos de SQL

```sql
SELECT DATE_ADD('2024-01-01', INTERVAL 30 DAY);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```

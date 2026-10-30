---
title: HOURS_ADD (Lakehouse v2)
description: HOURS_ADD — suma un número específico de horas a un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-add.md
---

Suma un número específico de horas a un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.hours_add(<datetime>, <n>)
```

## Ejemplos de Analyze

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
HOURS_ADD(<datetime>, <n>)
```

## Ejemplos de SQL

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```

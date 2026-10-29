---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — suma un número específico de minutos a un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

Suma un número específico de minutos a un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.minutes_add(<datetime>, <n>)
```

## Ejemplos de Analyze

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
MINUTES_ADD(<datetime>, <n>)
```

## Ejemplos de SQL

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```

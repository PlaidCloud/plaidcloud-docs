---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD — suma un número específico de segundos a un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

Suma un número específico de segundos a un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.seconds_add(<datetime>, <n>)
```

## Ejemplos de Analyze

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
SECONDS_ADD(<datetime>, <n>)
```

## Ejemplos de SQL

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```

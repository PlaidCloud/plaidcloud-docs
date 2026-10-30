---
title: MICROSECONDS_ADD (Lakehouse v2)
description: MICROSECONDS_ADD — suma un número específico de microsegundos a un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-add.md
---

Suma un número específico de microsegundos a un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.microseconds_add(<datetime>, <n>)
```

## Ejemplos de Analyze

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## Ejemplos de SQL

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```

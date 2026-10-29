---
title: HOUR (Lakehouse v2)
description: HOUR — devuelve la hora de un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hour.md
---

Devuelve la hora de un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.hour(<datetime>)
```

## Ejemplos de Analyze

```python
func.hour('2024-06-15 14:30:00')

┌────┐
│ 14  │
└────┘
```

## Sintaxis de SQL

```sql
HOUR(<datetime>)
```

## Ejemplos de SQL

```sql
SELECT HOUR('2024-06-15 14:30:00');

┌────┐
│ 14  │
└────┘
```

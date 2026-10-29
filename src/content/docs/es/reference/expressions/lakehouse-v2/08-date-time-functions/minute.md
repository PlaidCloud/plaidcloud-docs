---
title: MINUTE (Lakehouse v2)
description: MINUTE — devuelve el minuto de un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

Devuelve el minuto de un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.minute(<datetime>)
```

## Ejemplos de Analyze

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## Sintaxis de SQL

```sql
MINUTE(<datetime>)
```

## Ejemplos de SQL

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```

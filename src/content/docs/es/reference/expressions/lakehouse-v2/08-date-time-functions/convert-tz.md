---
title: CONVERT_TZ (Lakehouse v2)
description: CONVERT_TZ — convierte un valor de fecha y hora de una zona horaria a otra.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/convert-tz.md
---

Convierte un valor de fecha y hora de una zona horaria a otra.

## Sintaxis de Analyze

```python
func.convert_tz(<datetime>, <from_tz>, <to_tz>)
```

## Ejemplos de Analyze

```python
func.convert_tz('2024-01-01 12:00:00', 'UTC', 'America/New_York')

┌───────────────────────┐
│ '2024-01-01 07:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
CONVERT_TZ(<datetime>, <from_tz>, <to_tz>)
```

## Ejemplos de SQL

```sql
SELECT CONVERT_TZ('2024-01-01 12:00:00', 'UTC', 'America/New_York');

┌─────────────────────┐
│ 2024-01-01 07:00:00  │
└─────────────────────┘
```

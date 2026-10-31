---
title: TIME_FORMAT (Lakehouse v2)
description: TIME_FORMAT — da formato a un valor de hora según una cadena de formato.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-format.md
---

Da formato a un valor de hora según una cadena de formato.

## Sintaxis de Analyze

```python
func.time_format(<time>, <format>)
```

## Ejemplos de Analyze

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TIME_FORMAT(<time>, <format>)
```

## Ejemplos de SQL

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```

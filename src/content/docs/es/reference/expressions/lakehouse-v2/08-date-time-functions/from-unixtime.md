---
title: FROM_UNIXTIME (Lakehouse v2)
description: FROM_UNIXTIME — convierte una marca de tiempo Unix en una cadena de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-unixtime.md
---

Convierte una marca de tiempo Unix en una cadena de fecha y hora.

## Sintaxis de Analyze

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Ejemplos de Analyze

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## Ejemplos de SQL

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```

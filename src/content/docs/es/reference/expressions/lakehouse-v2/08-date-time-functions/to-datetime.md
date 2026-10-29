---
title: TO_DATETIME (Lakehouse v2)
description: TO_DATETIME — convierte un valor en un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime.md
---

Convierte un valor en un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.to_datetime(<expr>)
```

## Ejemplos de Analyze

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TO_DATETIME(<expr>)
```

## Ejemplos de SQL

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```

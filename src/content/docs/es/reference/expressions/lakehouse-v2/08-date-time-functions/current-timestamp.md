---
title: CURRENT_TIMESTAMP (Lakehouse v2)
description: CURRENT_TIMESTAMP — devuelve la fecha y la hora actuales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timestamp.md
---

Devuelve la fecha y la hora actuales.

## Sintaxis de Analyze

```python
func.current_timestamp()
```

## Ejemplos de Analyze

```python
func.current_timestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
CURRENT_TIMESTAMP()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME — devuelve la hora actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-time.md
---

Devuelve la hora actual.

## Sintaxis de Analyze

```python
func.current_time()
```

## Ejemplos de Analyze

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## Sintaxis de SQL

```sql
CURRENT_TIME()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```

---
title: UTC_TIME (Lakehouse v2)
description: UTC_TIME — devuelve la hora UTC actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-time.md
---

Devuelve la hora UTC actual.

## Sintaxis de Analyze

```python
func.utc_time()
```

## Ejemplos de Analyze

```python
func.utc_time()

┌────────────┐
│ '18:30:00'  │
└────────────┘
```

## Sintaxis de SQL

```sql
UTC_TIME()
```

## Ejemplos de SQL

```sql
SELECT UTC_TIME();

┌──────────┐
│ 18:30:00  │
└──────────┘
```

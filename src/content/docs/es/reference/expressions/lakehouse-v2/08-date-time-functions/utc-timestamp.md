---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP — devuelve la fecha y hora UTC actuales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

Devuelve la fecha y hora UTC actuales.

## Sintaxis de Analyze

```python
func.utc_timestamp()
```

## Ejemplos de Analyze

```python
func.utc_timestamp()

┌───────────────────────┐
│ '2024-06-15 18:30:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
UTC_TIMESTAMP()
```

## Ejemplos de SQL

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```

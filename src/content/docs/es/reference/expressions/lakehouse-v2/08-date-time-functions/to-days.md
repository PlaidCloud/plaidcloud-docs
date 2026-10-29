---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS — convierte una fecha en un recuento de días.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-days.md
---

Convierte una fecha en un recuento de días.

## Sintaxis de Analyze

```python
func.to_days(<date>)
```

## Ejemplos de Analyze

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## Sintaxis de SQL

```sql
TO_DAYS(<date>)
```

## Ejemplos de SQL

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```

---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS — convierte un recuento de días en una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-days.md
---

Convierte un recuento de días en una fecha.

## Sintaxis de Analyze

```python
func.from_days(<n>)
```

## Ejemplos de Analyze

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
FROM_DAYS(<n>)
```

## Ejemplos de SQL

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```

---
title: TO_DATE (Lakehouse v2)
description: TO_DATE — convierte un valor de fecha y hora en una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

Convierte un valor de fecha y hora en una fecha.

## Sintaxis de Analyze

```python
func.to_date(<datetime>)
```

## Ejemplos de Analyze

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
TO_DATE(<datetime>)
```

## Ejemplos de SQL

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

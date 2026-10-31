---
title: ADDDATE (Lakehouse v2)
description: ADDDATE — suma un intervalo de tiempo específico a una fecha. Alias de `DATE_ADD`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/adddate.md
---

Suma un intervalo de tiempo específico a una fecha. Alias de `DATE_ADD`.

## Sintaxis de Analyze

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Ejemplos de Analyze

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## Ejemplos de SQL

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```

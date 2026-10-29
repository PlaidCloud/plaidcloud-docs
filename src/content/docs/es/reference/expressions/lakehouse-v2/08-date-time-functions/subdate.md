---
title: SUBDATE (Lakehouse v2)
description: SUBDATE — resta un intervalo de tiempo de una fecha. Alias de `DATE_SUB`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/subdate.md
---

Resta un intervalo de tiempo de una fecha. Alias de `DATE_SUB`.

## Sintaxis de Analyze

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Ejemplos de Analyze

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## Ejemplos de SQL

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```

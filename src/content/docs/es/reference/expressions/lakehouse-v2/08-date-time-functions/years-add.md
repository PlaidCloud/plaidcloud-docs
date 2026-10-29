---
title: YEARS_ADD (Lakehouse v2)
description: YEARS_ADD — suma un número específico de años a una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-add.md
---

Suma un número específico de años a una fecha.

## Sintaxis de Analyze

```python
func.years_add(<date>, <n>)
```

## Ejemplos de Analyze

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
YEARS_ADD(<date>, <n>)
```

## Ejemplos de SQL

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```

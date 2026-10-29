---
title: MONTHS_ADD (Lakehouse v2)
description: MONTHS_ADD — suma un número específico de meses a una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-add.md
---

Suma un número específico de meses a una fecha.

## Sintaxis de Analyze

```python
func.months_add(<date>, <n>)
```

## Ejemplos de Analyze

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
MONTHS_ADD(<date>, <n>)
```

## Ejemplos de SQL

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```

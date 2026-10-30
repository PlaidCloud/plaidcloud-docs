---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD — suma un número específico de semanas a una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-add.md
---

Suma un número específico de semanas a una fecha.

## Sintaxis de Analyze

```python
func.weeks_add(<date>, <n>)
```

## Ejemplos de Analyze

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
WEEKS_ADD(<date>, <n>)
```

## Ejemplos de SQL

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```

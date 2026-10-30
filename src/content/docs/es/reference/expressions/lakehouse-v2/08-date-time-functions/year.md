---
title: YEAR (Lakehouse v2)
description: YEAR — devuelve el año de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/year.md
---

Devuelve el año de una fecha.

## Sintaxis de Analyze

```python
func.year(<date>)
```

## Ejemplos de Analyze

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## Sintaxis de SQL

```sql
YEAR(<date>)
```

## Ejemplos de SQL

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```

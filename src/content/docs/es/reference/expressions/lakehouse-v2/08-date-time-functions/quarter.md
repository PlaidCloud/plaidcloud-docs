---
title: QUARTER (Lakehouse v2)
description: QUARTER — devuelve el trimestre del año de una fecha (1-4).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/quarter.md
---

Devuelve el trimestre del año de una fecha (1-4).

## Sintaxis de Analyze

```python
func.quarter(<date>)
```

## Ejemplos de Analyze

```python
func.quarter('2024-06-15')

┌───┐
│ 2  │
└───┘
```

## Sintaxis de SQL

```sql
QUARTER(<date>)
```

## Ejemplos de SQL

```sql
SELECT QUARTER('2024-06-15');

┌───┐
│ 2  │
└───┘
```

---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK — devuelve el año y el número de semana de una fecha como un entero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

Devuelve el año y el número de semana de una fecha como un entero.

## Sintaxis de Analyze

```python
func.yearweek(<date>[, <mode>])
```

## Ejemplos de Analyze

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## Sintaxis de SQL

```sql
YEARWEEK(<date>[, <mode>])
```

## Ejemplos de SQL

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```

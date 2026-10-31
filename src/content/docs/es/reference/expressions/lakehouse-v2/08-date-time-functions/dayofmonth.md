---
title: DAYOFMONTH (Lakehouse v2)
description: DAYOFMONTH — devuelve el día del mes de una fecha. Alias de `DAY`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofmonth.md
---

Devuelve el día del mes de una fecha. Alias de `DAY`.

## Sintaxis de Analyze

```python
func.dayofmonth(<date>)
```

## Ejemplos de Analyze

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## Sintaxis de SQL

```sql
DAYOFMONTH(<date>)
```

## Ejemplos de SQL

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```

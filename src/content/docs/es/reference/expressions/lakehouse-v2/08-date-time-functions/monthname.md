---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME — devuelve el nombre del mes de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

Devuelve el nombre del mes de una fecha.

## Sintaxis de Analyze

```python
func.monthname(<date>)
```

## Ejemplos de Analyze

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## Sintaxis de SQL

```sql
MONTHNAME(<date>)
```

## Ejemplos de SQL

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```

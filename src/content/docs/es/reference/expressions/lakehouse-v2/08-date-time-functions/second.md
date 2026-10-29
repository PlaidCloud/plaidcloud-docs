---
title: SECOND (Lakehouse v2)
description: SECOND — devuelve el segundo de un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

Devuelve el segundo de un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.second(<datetime>)
```

## Ejemplos de Analyze

```python
func.second('2024-06-15 14:30:45')

┌────┐
│ 45  │
└────┘
```

## Sintaxis de SQL

```sql
SECOND(<datetime>)
```

## Ejemplos de SQL

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```

---
title: DATE (Lakehouse v2)
description: DATE — extrae la parte de fecha de una expresión de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date.md
---

Extrae la parte de fecha de una expresión de fecha y hora.

## Sintaxis de Analyze

```python
func.date(<datetime>)
```

## Ejemplos de Analyze

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
DATE(<datetime>)
```

## Ejemplos de SQL

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

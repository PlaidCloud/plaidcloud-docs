---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP — convierte una fecha o una cadena en un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestamp.md
---

Convierte una fecha o una cadena en un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.timestamp(<expr>)
```

## Ejemplos de Analyze

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TIMESTAMP(<expr>)
```

## Ejemplos de SQL

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```

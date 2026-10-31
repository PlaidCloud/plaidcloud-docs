---
title: TO_ISO8601 (Lakehouse v2)
description: TO_ISO8601 — convierte una fecha o un valor de fecha y hora en una cadena con formato ISO 8601.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-iso8601.md
---

Convierte una fecha o un valor de fecha y hora en una cadena con formato ISO 8601.

## Sintaxis de Analyze

```python
func.to_iso8601(<datetime>)
```

## Ejemplos de Analyze

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TO_ISO8601(<datetime>)
```

## Ejemplos de SQL

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```

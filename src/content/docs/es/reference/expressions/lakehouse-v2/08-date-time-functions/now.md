---
title: NOW (Lakehouse v2)
description: NOW — devuelve la fecha y hora actuales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

Devuelve la fecha y hora actuales.

## Sintaxis de Analyze

```python
func.now()
```

## Ejemplos de Analyze

```python
func.now()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
NOW()
```

## Ejemplos de SQL

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

---
title: LOCALTIME (Lakehouse v2)
description: LOCALTIME — devuelve la fecha y la hora actuales. Alias de `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtime.md
---

Devuelve la fecha y la hora actuales. Alias de `NOW`.

## Sintaxis de Analyze

```python
func.localtime()
```

## Ejemplos de Analyze

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
LOCALTIME()
```

## Ejemplos de SQL

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

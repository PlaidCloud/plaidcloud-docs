---
title: LOCALTIMESTAMP (Lakehouse v2)
description: LOCALTIMESTAMP — devuelve la fecha y la hora actuales. Alias de `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtimestamp.md
---

Devuelve la fecha y la hora actuales. Alias de `NOW`.

## Sintaxis de Analyze

```python
func.localtimestamp()
```

## Ejemplos de Analyze

```python
func.localtimestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
LOCALTIMESTAMP()
```

## Ejemplos de SQL

```sql
SELECT LOCALTIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

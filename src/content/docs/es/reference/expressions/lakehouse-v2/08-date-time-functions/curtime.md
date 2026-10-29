---
title: CURTIME (Lakehouse v2)
description: CURTIME — devuelve la hora actual. Alias de `CURRENT_TIME`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curtime.md
---

Devuelve la hora actual. Alias de `CURRENT_TIME`.

## Sintaxis de Analyze

```python
func.curtime()
```

## Ejemplos de Analyze

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## Sintaxis de SQL

```sql
CURTIME()
```

## Ejemplos de SQL

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```

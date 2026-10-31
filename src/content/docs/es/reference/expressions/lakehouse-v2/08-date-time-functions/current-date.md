---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE — devuelve la fecha actual. Alias de `CURDATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-date.md
---

Devuelve la fecha actual. Alias de `CURDATE`.

## Sintaxis de Analyze

```python
func.current_date()
```

## Ejemplos de Analyze

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
CURRENT_DATE()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

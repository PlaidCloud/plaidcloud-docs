---
title: CURDATE (Lakehouse v2)
description: CURDATE — devuelve la fecha actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curdate.md
---

Devuelve la fecha actual.

## Sintaxis de Analyze

```python
func.curdate()
```

## Ejemplos de Analyze

```python
func.curdate()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
CURDATE()
```

## Ejemplos de SQL

```sql
SELECT CURDATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

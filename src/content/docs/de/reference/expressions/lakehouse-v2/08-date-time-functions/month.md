---
title: MONTH (Lakehouse v2)
description: MONTH – gibt den Monat aus einem Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/month.md
---

Gibt den Monat aus einem Datum zurück.

## Analyze-Syntax

```python
func.month(<date>)
```

## Analyze-Beispiele

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQL-Syntax

```sql
MONTH(<date>)
```

## SQL-Beispiele

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```

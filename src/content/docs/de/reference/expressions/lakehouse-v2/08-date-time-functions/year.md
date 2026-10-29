---
title: YEAR (Lakehouse v2)
description: YEAR – gibt das Jahr aus einem Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/year.md
---

Gibt das Jahr aus einem Datum zurück.

## Analyze-Syntax

```python
func.year(<date>)
```

## Analyze-Beispiele

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## SQL-Syntax

```sql
YEAR(<date>)
```

## SQL-Beispiele

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```

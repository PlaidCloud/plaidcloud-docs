---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR – gibt den Tag des Jahres aus einem Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofyear.md
---

Gibt den Tag des Jahres aus einem Datum zurück.

## Analyze-Syntax

```python
func.dayofyear(<date>)
```

## Analyze-Beispiele

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## SQL-Syntax

```sql
DAYOFYEAR(<date>)
```

## SQL-Beispiele

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```

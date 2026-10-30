---
title: DAYOFMONTH (Lakehouse v2)
description: DAYOFMONTH – gibt den Tag des Monats aus einem Datum zurück. Alias für `DAY`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofmonth.md
---

Gibt den Tag des Monats aus einem Datum zurück. Alias für `DAY`.

## Analyze-Syntax

```python
func.dayofmonth(<date>)
```

## Analyze-Beispiele

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQL-Syntax

```sql
DAYOFMONTH(<date>)
```

## SQL-Beispiele

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```

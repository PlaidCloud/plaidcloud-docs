---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME – gibt den Namen des Monats für ein Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

Gibt den Namen des Monats für ein Datum zurück.

## Analyze-Syntax

```python
func.monthname(<date>)
```

## Analyze-Beispiele

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## SQL-Syntax

```sql
MONTHNAME(<date>)
```

## SQL-Beispiele

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```

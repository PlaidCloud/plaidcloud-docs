---
title: DAY (Lakehouse v2)
description: DAY – gibt den Tag des Monats aus einem Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/day.md
---

Gibt den Tag des Monats aus einem Datum zurück.

## Analyze-Syntax

```python
func.day(<date>)
```

## Analyze-Beispiele

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQL-Syntax

```sql
DAY(<date>)
```

## SQL-Beispiele

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```

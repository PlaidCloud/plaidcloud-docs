---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR – gibt die Kalenderwoche des Jahres für ein Datum zurück. Alias für `WEEK`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekofyear.md
---

Gibt die Kalenderwoche des Jahres für ein Datum zurück. Alias für `WEEK`.

## Analyze-Syntax

```python
func.weekofyear(<date>)
```

## Analyze-Beispiele

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL-Syntax

```sql
WEEKOFYEAR(<date>)
```

## SQL-Beispiele

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```

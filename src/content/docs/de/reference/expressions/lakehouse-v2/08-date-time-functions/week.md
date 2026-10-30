---
title: WEEK (Lakehouse v2)
description: WEEK – gibt die Kalenderwoche des Jahres für ein Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week.md
---

Gibt die Kalenderwoche des Jahres für ein Datum zurück.

## Analyze-Syntax

```python
func.week(<date>[, <mode>])
```

## Analyze-Beispiele

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL-Syntax

```sql
WEEK(<date>[, <mode>])
```

## SQL-Beispiele

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```

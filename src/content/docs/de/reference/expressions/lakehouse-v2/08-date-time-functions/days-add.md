---
title: DAYS_ADD (Lakehouse v2)
description: DAYS_ADD – addiert eine angegebene Anzahl von Tagen zu einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-add.md
---

Addiert eine angegebene Anzahl von Tagen zu einem Datum.

## Analyze-Syntax

```python
func.days_add(<date>, <n>)
```

## Analyze-Beispiele

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQL-Syntax

```sql
DAYS_ADD(<date>, <n>)
```

## SQL-Beispiele

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```

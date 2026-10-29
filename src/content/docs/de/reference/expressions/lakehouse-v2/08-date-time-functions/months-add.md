---
title: MONTHS_ADD (Lakehouse v2)
description: MONTHS_ADD – addiert eine angegebene Anzahl von Monaten zu einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-add.md
---

Addiert eine angegebene Anzahl von Monaten zu einem Datum.

## Analyze-Syntax

```python
func.months_add(<date>, <n>)
```

## Analyze-Beispiele

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
MONTHS_ADD(<date>, <n>)
```

## SQL-Beispiele

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```

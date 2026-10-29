---
title: DATEDIFF (Lakehouse v2)
description: DATEDIFF – gibt die Anzahl der Tage zwischen zwei Datumswerten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/datediff.md
---

Gibt die Anzahl der Tage zwischen zwei Datumswerten zurück.

## Analyze-Syntax

```python
func.datediff(<end_date>, <start_date>)
```

## Analyze-Beispiele

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## SQL-Syntax

```sql
DATEDIFF(<end_date>, <start_date>)
```

## SQL-Beispiele

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```

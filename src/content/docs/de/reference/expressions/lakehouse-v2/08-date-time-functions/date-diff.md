---
title: DATE_DIFF (Lakehouse v2)
description: DATE_DIFF – gibt die Differenz zwischen zwei Datumswerten in der angegebenen Einheit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-diff.md
---

Gibt die Differenz zwischen zwei Datumswerten in der angegebenen Einheit zurück.

## Analyze-Syntax

```python
func.date_diff(<unit>, <start>, <end>)
```

## Analyze-Beispiele

```python
func.date_diff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQL-Syntax

```sql
DATE_DIFF(<unit>, <start>, <end>)
```

## SQL-Beispiele

```sql
SELECT DATE_DIFF('DAY', '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```

---
title: DATE_DIFF (Lakehouse v2)
description: DATE_DIFF — zwraca różnicę między dwiema datami w podanej jednostce.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-diff.md
---

Zwraca różnicę między dwiema datami w podanej jednostce.

## Składnia Analyze

```python
func.date_diff(<unit>, <start>, <end>)
```

## Przykłady Analyze

```python
func.date_diff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## Składnia SQL

```sql
DATE_DIFF(<unit>, <start>, <end>)
```

## Przykłady SQL

```sql
SELECT DATE_DIFF('DAY', '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```

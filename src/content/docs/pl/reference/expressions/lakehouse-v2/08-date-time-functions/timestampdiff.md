---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — zwraca różnicę między dwiema datami i godzinami w podanej jednostce.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

Zwraca różnicę między dwiema datami i godzinami w podanej jednostce.

## Składnia Analyze

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Przykłady Analyze

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## Składnia SQL

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## Przykłady SQL

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```

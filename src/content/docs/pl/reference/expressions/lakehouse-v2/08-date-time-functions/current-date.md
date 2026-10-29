---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE — zwraca bieżącą datę. Alias funkcji `CURDATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-date.md
---

Zwraca bieżącą datę. Alias funkcji `CURDATE`.

## Składnia Analyze

```python
func.current_date()
```

## Przykłady Analyze

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Składnia SQL

```sql
CURRENT_DATE()
```

## Przykłady SQL

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

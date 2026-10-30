---
title: CURDATE (Lakehouse v2)
description: CURDATE — zwraca bieżącą datę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curdate.md
---

Zwraca bieżącą datę.

## Składnia Analyze

```python
func.curdate()
```

## Przykłady Analyze

```python
func.curdate()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Składnia SQL

```sql
CURDATE()
```

## Przykłady SQL

```sql
SELECT CURDATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

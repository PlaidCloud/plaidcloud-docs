---
title: MINUTE (Lakehouse v2)
description: MINUTE — zwraca minutę z daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

Zwraca minutę z daty i godziny.

## Składnia Analyze

```python
func.minute(<datetime>)
```

## Przykłady Analyze

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## Składnia SQL

```sql
MINUTE(<datetime>)
```

## Przykłady SQL

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```

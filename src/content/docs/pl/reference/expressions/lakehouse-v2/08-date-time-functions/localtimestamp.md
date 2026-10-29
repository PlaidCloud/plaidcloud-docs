---
title: LOCALTIMESTAMP (Lakehouse v2)
description: LOCALTIMESTAMP — zwraca bieżącą datę i godzinę. Alias funkcji `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtimestamp.md
---

Zwraca bieżącą datę i godzinę. Alias funkcji `NOW`.

## Składnia Analyze

```python
func.localtimestamp()
```

## Przykłady Analyze

```python
func.localtimestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
LOCALTIMESTAMP()
```

## Przykłady SQL

```sql
SELECT LOCALTIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

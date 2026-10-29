---
title: LOCALTIME (Lakehouse v2)
description: LOCALTIME — zwraca bieżącą datę i godzinę. Alias funkcji `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtime.md
---

Zwraca bieżącą datę i godzinę. Alias funkcji `NOW`.

## Składnia Analyze

```python
func.localtime()
```

## Przykłady Analyze

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
LOCALTIME()
```

## Przykłady SQL

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```

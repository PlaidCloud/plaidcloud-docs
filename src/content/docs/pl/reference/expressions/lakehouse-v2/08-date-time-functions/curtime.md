---
title: CURTIME (Lakehouse v2)
description: CURTIME — zwraca bieżący czas. Alias funkcji `CURRENT_TIME`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curtime.md
---

Zwraca bieżący czas. Alias funkcji `CURRENT_TIME`.

## Składnia Analyze

```python
func.curtime()
```

## Przykłady Analyze

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## Składnia SQL

```sql
CURTIME()
```

## Przykłady SQL

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```

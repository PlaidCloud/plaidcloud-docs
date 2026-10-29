---
title: TODAY (Lakehouse v1)
description: TODAY — zwraca bieżącą datę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/today.md
---

Zwraca bieżącą datę.

## Składnia Analyze

```python
func.today()
```

## Przykłady Analyze

```python
func.today()
┌──────────────┐
│ func.today() │
├──────────────┤
│ 2021-09-03   │
└──────────────┘
```

## Składnia SQL

```sql
TODAY()
```

## Typ zwracany

`DATE`, zwraca datę w formacie „YYYY-MM-DD”.

## Przykłady SQL

```sql
SELECT TODAY();
┌────────────┐
│ TODAY()    │
├────────────┤
│ 2021-09-03 │
└────────────┘
```

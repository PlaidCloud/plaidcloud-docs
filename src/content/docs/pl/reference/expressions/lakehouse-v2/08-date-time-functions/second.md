---
title: SECOND (Lakehouse v2)
description: SECOND — zwraca sekundę z daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

Zwraca sekundę z daty i godziny.

## Składnia Analyze

```python
func.second(<datetime>)
```

## Przykłady Analyze

```python
func.second('2024-06-15 14:30:45')

┌────┐
│ 45  │
└────┘
```

## Składnia SQL

```sql
SECOND(<datetime>)
```

## Przykłady SQL

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```

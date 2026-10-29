---
title: DATE_TRUNC (Lakehouse v2)
description: DATE_TRUNC — obcina wartość daty lub daty i godziny do podanej precyzji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-trunc.md
---

Obcina wartość daty lub daty i godziny do podanej precyzji.

## Składnia Analyze

```python
func.date_trunc(<unit>, <datetime>)
```

## Przykłady Analyze

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## Składnia SQL

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## Przykłady SQL

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```

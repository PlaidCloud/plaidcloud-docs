---
title: TO_DATE (Lakehouse v2)
description: TO_DATE — konwertuje datę i godzinę na datę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

Konwertuje datę i godzinę na datę.

## Składnia Analyze

```python
func.to_date(<datetime>)
```

## Przykłady Analyze

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Składnia SQL

```sql
TO_DATE(<datetime>)
```

## Przykłady SQL

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

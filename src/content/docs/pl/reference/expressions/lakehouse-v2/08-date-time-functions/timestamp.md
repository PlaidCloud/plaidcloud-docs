---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP — konwertuje datę lub ciąg znaków na datę i godzinę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestamp.md
---

Konwertuje datę lub ciąg znaków na datę i godzinę.

## Składnia Analyze

```python
func.timestamp(<expr>)
```

## Przykłady Analyze

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
TIMESTAMP(<expr>)
```

## Przykłady SQL

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```

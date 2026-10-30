---
title: FROM_UNIXTIME (Lakehouse v2)
description: FROM_UNIXTIME — konwertuje znacznik czasu Unix na ciąg daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-unixtime.md
---

Konwertuje znacznik czasu Unix na ciąg daty i godziny.

## Składnia Analyze

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Przykłady Analyze

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## Przykłady SQL

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```

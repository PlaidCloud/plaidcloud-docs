---
title: UNIX_TIMESTAMP (Lakehouse v2)
description: UNIX_TIMESTAMP — konwertuje datę i godzinę na znacznik czasu Unix.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/unix-timestamp.md
---

Konwertuje datę i godzinę na znacznik czasu Unix.

## Składnia Analyze

```python
func.unix_timestamp([<datetime>])
```

## Przykłady Analyze

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## Składnia SQL

```sql
UNIX_TIMESTAMP([<datetime>])
```

## Przykłady SQL

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```

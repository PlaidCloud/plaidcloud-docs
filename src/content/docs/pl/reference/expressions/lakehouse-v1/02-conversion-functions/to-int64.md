---
title: TO_INT64 (Lakehouse v1)
description: TO_INT64 — konwertuje wartość na typ danych INT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int64.md
---

Konwertuje wartość na typ danych INT64.

## Składnia Analyze

```python
func.to_int64( <expr> )
```

## Przykłady Analyze

```python
func.to_int64('123')

┌──────────────────────┐
│ func.to_int64('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Składnia SQL

```sql
TO_INT64( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_INT64('123');

┌─────────────────┐
│ to_int64('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```

---
title: TO_INT16 (Lakehouse v1)
description: TO_INT16 — konwertuje wartość na typ danych INT16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int16.md
---

Konwertuje wartość na typ danych INT16.

## Składnia Analyze

```python
func.to_int16( <expr> )
```

## Przykłady Analyze

```python
func.to_int16('123')

┌──────────────────────┐
│ func.to_int16('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Składnia SQL

```sql
TO_INT16( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_INT16('123');

┌─────────────────┐
│ to_int16('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```

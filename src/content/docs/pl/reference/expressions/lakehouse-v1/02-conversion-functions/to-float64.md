---
title: TO_FLOAT64 (Lakehouse v1)
description: TO_FLOAT64 — konwertuje wartość na typ danych FLOAT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float64.md
---

Konwertuje wartość na typ danych FLOAT64.

## Składnia Analyze

```python
func.to_float64( <expr> )
```

## Przykłady Analyze

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Składnia SQL

```sql
TO_FLOAT64( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```

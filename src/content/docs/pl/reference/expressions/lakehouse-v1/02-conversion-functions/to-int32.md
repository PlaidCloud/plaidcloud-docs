---
title: TO_INT32 (Lakehouse v1)
description: TO_INT32 — konwertuje wartość na typ danych INT32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int32.md
---

Konwertuje wartość na typ danych INT32.

## Składnia Analyze

```python
func.to_int32( <expr> )
```

## Przykłady Analyze

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Składnia SQL

```sql
TO_INT32( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```

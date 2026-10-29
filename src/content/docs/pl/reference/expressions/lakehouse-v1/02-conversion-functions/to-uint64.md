---
title: TO_UINT64 (Lakehouse v1)
description: TO_UINT64 — konwertuje wartość na typ danych UINT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint64.md
---

Konwertuje wartość na typ danych UINT64.

## Składnia Analyze

```python
func.to_uint64( <expr> )
```

## Przykłady Analyze

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Składnia SQL

```sql
TO_UINT64( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```

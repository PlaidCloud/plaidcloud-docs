---
title: TO_INT8 (Lakehouse v1)
description: TO_INT8 — konwertuje wartość na typ danych INT8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int8.md
---

Konwertuje wartość na typ danych INT8.

## Składnia Analyze

```python
func.to_int8( <expr> )
```

## Przykłady Analyze

```python
func.to_int8('123')

┌─────────────────────┐
│ func.to_int8('123') │
├─────────────────────┤
│                 123 │
└─────────────────────┘
```

## Składnia SQL

```sql
TO_INT8( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```

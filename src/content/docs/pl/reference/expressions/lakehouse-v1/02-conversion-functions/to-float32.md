---
title: TO_FLOAT32 (Lakehouse v1)
description: TO_FLOAT32 — konwertuje wartość na typ danych FLOAT32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float32.md
---

Konwertuje wartość na typ danych FLOAT32.

## Składnia Analyze

```python
func.to_float32( <expr> )
```

## Przykłady Analyze

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Składnia SQL

```sql
TO_FLOAT32( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```

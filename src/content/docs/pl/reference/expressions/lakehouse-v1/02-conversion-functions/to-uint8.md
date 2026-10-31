---
title: TO_UINT8 (Lakehouse v1)
description: TO_UINT8 — konwertuje wartość na typ danych UINT8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint8.md
---

Konwertuje wartość na typ danych UINT8.

## Składnia Analyze

```python
func.to_uint8( <expr> )
```

## Przykłady Analyze

```python
func.to_uint8('123')

┌──────────────────────┐
│ func.to_uint8('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Składnia SQL

```sql
TO_UINT8( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_UINT8('123');

┌─────────────────┐
│ to_uint8('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```

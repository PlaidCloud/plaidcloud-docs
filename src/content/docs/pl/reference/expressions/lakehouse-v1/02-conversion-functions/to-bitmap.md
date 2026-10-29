---
title: TO_BITMAP (Lakehouse v1)
description: TO_BITMAP — konwertuje wartość na typ danych BITMAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-bitmap.md
---

Konwertuje wartość na typ danych BITMAP.

## Składnia Analyze

```python
func.to_bitmap( <expr> )
```

## Przykłady Analyze

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## Składnia SQL

```sql
TO_BITMAP( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```

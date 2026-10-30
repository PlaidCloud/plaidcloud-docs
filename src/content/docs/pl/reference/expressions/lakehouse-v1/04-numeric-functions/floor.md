---
title: FLOOR (Lakehouse v1)
description: FLOOR — zaokrągla liczbę w dół.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/floor.md
---

Zaokrągla liczbę w dół.

## Składnia Analyze

```python
func.floor( <x> )
```

## Przykłady Analyze

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## Składnia SQL

```sql
FLOOR( <x> )
```

## Przykłady SQL

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```

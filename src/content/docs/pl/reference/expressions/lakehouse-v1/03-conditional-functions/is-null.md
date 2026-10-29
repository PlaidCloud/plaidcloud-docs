---
title: IS_NULL (Lakehouse v1)
description: IS_NULL — sprawdza, czy wartość jest NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-null.md
---

Sprawdza, czy wartość jest NULL.

## Składnia Analyze

```python
func.is_null(<expr>)
```

## Przykłady Analyze

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## Składnia SQL

```sql
IS_NULL(<expr>)
```

## Przykłady SQL

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```

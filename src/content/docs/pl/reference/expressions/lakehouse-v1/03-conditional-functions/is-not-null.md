---
title: IS_NOT_NULL (Lakehouse v1)
description: IS_NOT_NULL — sprawdza, czy wartość nie jest NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-null.md
---

Sprawdza, czy wartość nie jest NULL.

## Składnia Analyze

```python
func.is_not_null(<expr>)
```

## Przykłady Analyze

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## Składnia SQL

```sql
IS_NOT_NULL(<expr>)
```

## Przykłady SQL

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```

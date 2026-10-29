---
title: RIGHT (Lakehouse v2)
description: RIGHT — zwraca N ostatnich znaków od prawej strony ciągu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

Zwraca N ostatnich znaków od prawej strony ciągu.

## Składnia Analyze

```python
func.right(<str>, <len>)
```

## Przykłady Analyze

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Składnia SQL

```sql
RIGHT(<str>, <len>)
```

## Przykłady SQL

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```

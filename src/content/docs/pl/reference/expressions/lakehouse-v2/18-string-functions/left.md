---
title: LEFT (Lakehouse v2)
description: LEFT — zwraca N pierwszych znaków od lewej strony ciągu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

Zwraca N pierwszych znaków od lewej strony ciągu.

## Składnia Analyze

```python
func.left(<str>, <len>)
```

## Przykłady Analyze

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Składnia SQL

```sql
LEFT(<str>, <len>)
```

## Przykłady SQL

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```

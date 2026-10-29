---
title: SQUARE (Lakehouse v2)
description: SQUARE — zwraca kwadrat liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

Zwraca kwadrat liczby.

## Składnia Analyze

```python
func.square(<x>)
```

## Przykłady Analyze

```python
func.square(7)

┌────┐
│ 49  │
└────┘
```

## Składnia SQL

```sql
SQUARE(<x>)
```

## Przykłady SQL

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```

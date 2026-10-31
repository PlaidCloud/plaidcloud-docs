---
title: DROUND (Lakehouse v2)
description: DROUND — alias funkcji `ROUND`. Zobacz [ROUND](../round/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dround.md
---

Alias funkcji `ROUND`. Zobacz [ROUND](../round/).

## Składnia Analyze

```python
func.dround(3.14159, 2)
```

## Przykłady Analyze

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## Składnia SQL

```sql
DROUND(<x>)
```

## Przykłady SQL

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```

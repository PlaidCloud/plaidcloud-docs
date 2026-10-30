---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY — zwraca iloczyn dwóch liczb.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/multiply.md
---

Zwraca iloczyn dwóch liczb.

## Składnia Analyze

```python
func.multiply(<x>, <y>)
```

## Przykłady Analyze

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## Składnia SQL

```sql
MULTIPLY(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```

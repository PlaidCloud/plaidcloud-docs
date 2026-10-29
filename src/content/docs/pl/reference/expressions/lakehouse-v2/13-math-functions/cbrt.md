---
title: CBRT (Lakehouse v2)
description: CBRT — zwraca pierwiastek sześcienny liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

Zwraca pierwiastek sześcienny liczby.

## Składnia Analyze

```python
func.cbrt(<x>)
```

## Przykłady Analyze

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## Składnia SQL

```sql
CBRT(<x>)
```

## Przykłady SQL

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```

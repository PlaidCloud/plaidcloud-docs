---
title: SQRT (Lakehouse v2)
description: SQRT — zwraca pierwiastek kwadratowy liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sqrt.md
---

Zwraca pierwiastek kwadratowy liczby.

## Składnia Analyze

```python
func.sqrt(<x>)
```

## Przykłady Analyze

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## Składnia SQL

```sql
SQRT(<x>)
```

## Przykłady SQL

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```

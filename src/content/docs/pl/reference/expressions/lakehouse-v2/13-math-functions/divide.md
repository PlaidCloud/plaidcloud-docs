---
title: DIVIDE (Lakehouse v2)
description: DIVIDE — zwraca wynik dzielenia jednej liczby przez drugą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

Zwraca wynik dzielenia jednej liczby przez drugą.

## Składnia Analyze

```python
func.divide(<x>, <y>)
```

## Przykłady Analyze

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## Składnia SQL

```sql
DIVIDE(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

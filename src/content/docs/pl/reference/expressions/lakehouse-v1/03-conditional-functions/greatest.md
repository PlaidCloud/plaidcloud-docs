---
title: GREATEST (Lakehouse v1)
description: GREATEST — zwraca największą wartość z zestawu wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/greatest.md
---

Zwraca największą wartość z zestawu wartości.

## Składnia Analyze

```python
func.greatest(<value1>, <value2> ...)
```

## Przykłady Analyze

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## Składnia SQL

```sql
GREATEST(<value1>, <value2> ...)
```

## Przykłady SQL

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```

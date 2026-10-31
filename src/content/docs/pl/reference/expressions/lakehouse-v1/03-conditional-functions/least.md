---
title: LEAST (Lakehouse v1)
description: LEAST — zwraca najmniejszą wartość z zestawu wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/least.md
---

Zwraca najmniejszą wartość z zestawu wartości.

## Składnia Analyze

```python
func.least((<value1>, <value2> ...))
```

## Przykłady Analyze

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## Składnia SQL

```sql
LEAST(<value1>, <value2> ...)
```

## Przykłady SQL

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```

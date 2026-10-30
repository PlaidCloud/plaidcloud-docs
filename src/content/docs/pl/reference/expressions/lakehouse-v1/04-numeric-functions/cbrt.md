---
title: CBRT (Lakehouse v1)
description: CBRT — zwraca pierwiastek sześcienny z nieujemnej liczby x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cbrt.md
---

Zwraca pierwiastek sześcienny z nieujemnej liczby `x`.

## Składnia Analyze

```python
func.cbrt( <x> )
```

## Przykłady Analyze

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## Składnia SQL

```sql
CBRT( <x> )
```

## Przykłady SQL

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```

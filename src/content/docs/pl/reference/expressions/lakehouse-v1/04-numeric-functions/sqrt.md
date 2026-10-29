---
title: SQRT (Lakehouse v1)
description: SQRT — zwraca pierwiastek kwadratowy z nieujemnej liczby x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sqrt.md
---

Zwraca pierwiastek kwadratowy z nieujemnej liczby `x`. Dla ujemnych danych wejściowych zwraca NaN.

## Składnia Analyze

```python
func.sqrt( <x> )
```

## Przykłady Analyze

```python
func.sqrt(4)

┌──────────────┐
│ func.sqrt(4) │
├──────────────┤
│            2 │
└──────────────┘
```

## Składnia SQL

```sql
SQRT( <x> )
```

## Przykłady SQL

```sql
SELECT SQRT(4);

┌─────────┐
│ sqrt(4) │
├─────────┤
│       2 │
└─────────┘
```

---
title: PLUS (Lakehouse v1)
description: PLUS — oblicza sumę dwóch wartości liczbowych lub dziesiętnych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/plus.md
---

Oblicza sumę dwóch wartości liczbowych lub dziesiętnych.

## Składnia Analyze

```python
func.plus(<number1>, <number2>)
```

## Przykłady Analyze

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## Składnia SQL

```sql
PLUS(<number1>, <number2>)
```

## Aliasy

- [ADD](../add)

## Przykłady SQL

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```

---
title: PI (Lakehouse v1)
description: PI — zwraca wartość liczby π jako liczbę zmiennoprzecinkową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

Zwraca wartość liczby π jako liczbę zmiennoprzecinkową.

## Składnia Analyze

```python
func.pi()
```

## Przykłady Analyze

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## Składnia SQL

```sql
PI()
```

## Przykłady SQL

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

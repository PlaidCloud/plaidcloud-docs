---
title: PMOD (Lakehouse v2)
description: PMOD — zwraca dodatnią resztę z dzielenia dwóch liczb.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

Zwraca dodatnią resztę z dzielenia dwóch liczb.

## Składnia Analyze

```python
func.pmod(<x>, <y>)
```

## Przykłady Analyze

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## Składnia SQL

```sql
PMOD(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```

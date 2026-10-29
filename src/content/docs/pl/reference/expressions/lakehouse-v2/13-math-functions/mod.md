---
title: MOD (Lakehouse v2)
description: MOD — zwraca resztę z dzielenia dwóch liczb.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

Zwraca resztę z dzielenia dwóch liczb.

## Składnia Analyze

```python
func.mod(<x>, <y>)
```

## Przykłady Analyze

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
MOD(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```

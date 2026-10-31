---
title: ASIN (Lakehouse v1)
description: ASIN — zwraca arcus sinus x, czyli wartość, której sinus wynosi x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/asin.md
---

Zwraca arcus sinus `x`, czyli wartość, której sinus wynosi `x`. Zwraca NULL, jeśli `x` nie mieści się w zakresie od -1 do 1.

## Składnia Analyze

```python
func.asin( <x> )
```

## Przykłady Analyze

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## Składnia SQL

```sql
ASIN( <x> )
```

## Przykłady SQL

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

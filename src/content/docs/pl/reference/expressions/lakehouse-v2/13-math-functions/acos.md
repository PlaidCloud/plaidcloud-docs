---
title: ACOS (Lakehouse v2)
description: ACOS — zwraca arcus cosinus liczby w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/acos.md
---

Zwraca arcus cosinus liczby w radianach.

## Składnia Analyze

```python
func.acos(<x>)
```

## Przykłady Analyze

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## Składnia SQL

```sql
ACOS(<x>)
```

## Przykłady SQL

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

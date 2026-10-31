---
title: ASIN (Lakehouse v2)
description: ASIN — zwraca arcus sinus liczby w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/asin.md
---

Zwraca arcus sinus liczby w radianach.

## Składnia Analyze

```python
func.asin(<x>)
```

## Przykłady Analyze

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## Składnia SQL

```sql
ASIN(<x>)
```

## Przykłady SQL

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

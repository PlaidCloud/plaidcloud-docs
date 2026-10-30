---
title: ATAN (Lakehouse v2)
description: ATAN — zwraca arcus tangens liczby w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

Zwraca arcus tangens liczby w radianach.

## Składnia Analyze

```python
func.atan(<x>)
```

## Przykłady Analyze

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## Składnia SQL

```sql
ATAN(<x>)
```

## Przykłady SQL

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

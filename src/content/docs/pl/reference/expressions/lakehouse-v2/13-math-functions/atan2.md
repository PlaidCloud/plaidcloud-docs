---
title: ATAN2 (Lakehouse v2)
description: ATAN2 — zwraca arcus tangens y/x, określając ćwiartkę na podstawie znaków argumentów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan2.md
---

Zwraca arcus tangens y/x, określając ćwiartkę na podstawie znaków argumentów.

## Składnia Analyze

```python
func.atan2(<y>, <x>)
```

## Przykłady Analyze

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## Składnia SQL

```sql
ATAN2(<y>, <x>)
```

## Przykłady SQL

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

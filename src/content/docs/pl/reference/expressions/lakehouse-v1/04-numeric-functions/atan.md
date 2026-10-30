---
title: ATAN (Lakehouse v1)
description: ATAN — zwraca arcus tangens x, czyli wartość, której tangens wynosi x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan.md
---

Zwraca arcus tangens `x`, czyli wartość, której tangens wynosi `x`.

## Składnia Analyze

```python
func.atan( <x> )
```

## Przykłady Analyze

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## Składnia SQL

```sql
ATAN( <x> )
```

## Przykłady SQL

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

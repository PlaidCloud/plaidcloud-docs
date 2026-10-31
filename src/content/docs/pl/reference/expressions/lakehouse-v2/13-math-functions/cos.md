---
title: COS (Lakehouse v2)
description: COS — zwraca cosinus liczby w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

Zwraca cosinus liczby w radianach.

## Składnia Analyze

```python
func.cos(<x>)
```

## Przykłady Analyze

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## Składnia SQL

```sql
COS(<x>)
```

## Przykłady SQL

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```

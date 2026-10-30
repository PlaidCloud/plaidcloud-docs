---
title: ISNOTNULL (Lakehouse v2)
description: ISNOTNULL — sprawdza, czy wartość nie jest NULL. Zwraca 1, jeśli nie jest NULL, w przeciwnym razie 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnotnull.md
---

Sprawdza, czy wartość nie jest NULL. Zwraca 1, jeśli nie jest NULL, w przeciwnym razie 0.

## Składnia Analyze

```python
func.isnotnull(<expr>)
```

## Przykłady Analyze

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
ISNOTNULL(<expr>)
```

## Przykłady SQL

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```

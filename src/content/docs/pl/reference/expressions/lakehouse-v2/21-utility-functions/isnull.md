---
title: ISNULL (Lakehouse v2)
description: ISNULL — sprawdza, czy wartość jest NULL. Zwraca 1, jeśli jest NULL, w przeciwnym razie 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnull.md
---

Sprawdza, czy wartość jest NULL. Zwraca 1, jeśli jest NULL, w przeciwnym razie 0.

## Składnia Analyze

```python
func.isnull(<expr>)
```

## Przykłady Analyze

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
ISNULL(<expr>)
```

## Przykłady SQL

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```

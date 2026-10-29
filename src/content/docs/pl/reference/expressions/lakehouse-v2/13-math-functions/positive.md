---
title: POSITIVE (Lakehouse v2)
description: POSITIVE — zwraca wartość bez zmian (jednoargumentowy plus).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

Zwraca wartość bez zmian (jednoargumentowy plus).

## Składnia Analyze

```python
func.positive(<x>)
```

## Przykłady Analyze

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## Składnia SQL

```sql
POSITIVE(<x>)
```

## Przykłady SQL

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```

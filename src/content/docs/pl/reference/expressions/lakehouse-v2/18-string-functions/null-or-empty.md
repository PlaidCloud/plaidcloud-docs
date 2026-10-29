---
title: NULL_OR_EMPTY (Lakehouse v2)
description: NULL_OR_EMPTY — sprawdza, czy ciąg ma wartość NULL lub jest pusty. Zwraca 1, jeśli tak, w przeciwnym razie 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/null-or-empty.md
---

Sprawdza, czy ciąg ma wartość NULL lub jest pusty. Zwraca 1, jeśli tak, w przeciwnym razie 0.

## Składnia Analyze

```python
func.null_or_empty(<str>)
```

## Przykłady Analyze

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
NULL_OR_EMPTY(<str>)
```

## Przykłady SQL

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```

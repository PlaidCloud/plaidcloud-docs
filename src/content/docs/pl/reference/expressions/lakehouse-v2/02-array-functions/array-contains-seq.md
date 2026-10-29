---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ — sprawdza, czy tablica zawiera wszystkie elementy innej tablicy w tej samej kolejności.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

Sprawdza, czy tablica zawiera wszystkie elementy innej tablicy w tej samej kolejności.

## Składnia Analyze

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Przykłady Analyze

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## Przykłady SQL

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```

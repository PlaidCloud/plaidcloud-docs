---
title: FIND_IN_SET (Lakehouse v2)
description: FIND_IN_SET — zwraca pozycję ciągu na liście rozdzielonej przecinkami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/find-in-set.md
---

Zwraca pozycję ciągu na liście rozdzielonej przecinkami.

## Składnia Analyze

```python
func.find_in_set(<str>, <strlist>)
```

## Przykłady Analyze

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## Składnia SQL

```sql
FIND_IN_SET(<str>, <strlist>)
```

## Przykłady SQL

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```

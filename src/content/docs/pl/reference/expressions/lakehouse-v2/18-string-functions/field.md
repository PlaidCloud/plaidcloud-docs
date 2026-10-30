---
title: FIELD (Lakehouse v2)
description: FIELD — zwraca pozycję indeksu wartości na liście argumentów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

Zwraca pozycję indeksu wartości na liście argumentów.

## Składnia Analyze

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Przykłady Analyze

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## Składnia SQL

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## Przykłady SQL

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```

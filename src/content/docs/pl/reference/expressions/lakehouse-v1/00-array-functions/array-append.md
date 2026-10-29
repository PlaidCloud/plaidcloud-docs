---
title: ARRAY_APPEND (Lakehouse v1)
description: ARRAY_APPEND — dodaje element na początku tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-append.md
---

Dodaje element na początku tablicy.

## Składnia Analyze

```python
func.array_append( <array>, <element>)
```

## Przykłady Analyze

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_APPEND( <array>, <element>)
```

## Przykłady SQL

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```

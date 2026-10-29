---
title: ARRAY_TO_STRING (Lakehouse v1)
description: ARRAY_TO_STRING — łączy elementy tablicy w jeden ciąg znaków, używając podanego separatora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-to-string.md
---

Łączy elementy tablicy w jeden ciąg znaków, używając podanego separatora.

## Składnia Analyze

```python
func.array_to_string( <array>, '<separator>' )
```

## Przykłady Analyze

```python
func.array_to_string(['apple', 'banana', 'cherry'], ', ') 

┌────────────────────────────────────────────────────────────┐
│ func.array_to_string(['apple', 'banana', 'cherry'], ', ')  │
├────────────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                      │
└────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## Przykłady SQL

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```

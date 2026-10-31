---
title: ARRAY_TO_STRING (Lakehouse v1)
description: ARRAY_TO_STRING – verkettet die Elemente eines Arrays mit einem angegebenen Trennzeichen zu einer einzelnen Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-to-string.md
---

Verkettet die Elemente eines Arrays mit einem angegebenen Trennzeichen zu einer einzelnen Zeichenfolge.

## Analyze-Syntax

```python
func.array_to_string( <array>, '<separator>' )
```

## Analyze-Beispiele

```python
func.array_to_string(['apple', 'banana', 'cherry'], ', ') 

┌────────────────────────────────────────────────────────────┐
│ func.array_to_string(['apple', 'banana', 'cherry'], ', ')  │
├────────────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                      │
└────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## SQL-Beispiele

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```

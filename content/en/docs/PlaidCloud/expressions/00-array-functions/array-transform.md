---
title: ARRAY_TRANSFORM
---

Returns an array that is the result of applying the lambda function to each element of the input array.

## Analyze Syntax

```python
func.array_transform( <array>, <lambda> )
```

## Analyze Examples

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## Aliases

- [ARRAY_APPLY](../array-apply)

## SQL Examples

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
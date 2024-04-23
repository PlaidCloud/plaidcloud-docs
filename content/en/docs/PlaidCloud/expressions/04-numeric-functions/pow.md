---
title: POW
---

Returns the value of `x` to the power of `y`. 

## Analyze Syntax

```python
func.pow( <x, y> )
```

## Analyze Examples

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## SQL Syntax

```sql
POW( <x, y> )
```

## Aliases

- [POWER](../power)

## SQL Examples

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```
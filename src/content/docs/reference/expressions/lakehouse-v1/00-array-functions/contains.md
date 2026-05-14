---
title: CONTAINS
description: "Learn how to use the CONTAINS array function in PlaidCloud Lakehouse. Checks if the array contains a specific element. Includes syntax and examples."
---

Checks if the array contains a specific element.


## Analyze Syntax

```python
func.contains( <array>, <element> )
```

## Analyze Examples

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## SQL Syntax

```sql
CONTAINS( <array>, <element> )
```

## Aliases

- [ARRAY_CONTAINS](../array-contains)

## SQL Examples

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```

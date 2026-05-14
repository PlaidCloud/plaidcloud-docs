---
title: CBRT
description: "Learn how to use the CBRT numeric function in PlaidCloud Lakehouse. Returns the cube root of a nonnegative number x. Includes syntax and examples."
---

Returns the cube root of a nonnegative number `x`.

## Analyze Syntax

```python
func.cbrt( <x> )
```

## Analyze Examples

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## SQL Syntax

```sql
CBRT( <x> )
```

## SQL Examples

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```

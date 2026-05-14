---
title: CHAR
description: "Learn how to use the CHAR string function in PlaidCloud Lakehouse. Returns the character for a given ASCII code - see syntax, examples, and output."
---

Returns the character for a given ASCII code.

## Analyze Syntax

```python
func.char(<code>)
```

## Analyze Examples

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## SQL Syntax

```sql
CHAR(<code>)
```

## SQL Examples

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```

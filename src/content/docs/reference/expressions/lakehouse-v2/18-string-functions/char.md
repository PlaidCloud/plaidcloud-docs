---
title: CHAR (Lakehouse v2)
description: CHAR — returns the character for a given ASCII code.
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

---
title: SPACE
description: "Learn how to use the SPACE string function in PlaidCloud Lakehouse. Returns a string consisting of a specified number of spaces - with syntax and examples."
---

Returns a string consisting of a specified number of spaces.

## Analyze Syntax

```python
func.space(<n>)
```

## Analyze Examples

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## SQL Syntax

```sql
SPACE(<n>)
```

## SQL Examples

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```

---
title: ASCII
description: "Learn how to use the ASCII string function in PlaidCloud Lakehouse. Returns the ASCII code of the first character in a string - with syntax and examples."
---

Returns the ASCII code of the first character in a string.

## Analyze Syntax

```python
func.ascii(<str>)
```

## Analyze Examples

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## SQL Syntax

```sql
ASCII(<str>)
```

## SQL Examples

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```

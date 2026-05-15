---
title: ASCII (Lakehouse v2)
description: ASCII — Returns the ASCII code of the first character in a string.
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

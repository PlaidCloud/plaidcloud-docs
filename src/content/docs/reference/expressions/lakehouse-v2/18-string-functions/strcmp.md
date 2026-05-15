---
title: STRCMP (Lakehouse v2)
description: "Use the STRCMP string function in PlaidCloud Lakehouse. Compares two strings lexicographically. Returns 0 if equal, -1 if str1 < str2, 1 if str1 > str2."
---

Compares two strings lexicographically. Returns 0 if equal, -1 if str1 &lt; str2, 1 if str1 > str2.

## Analyze Syntax

```python
func.strcmp(<str1>, <str2>)
```

## Analyze Examples

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## SQL Syntax

```sql
STRCMP(<str1>, <str2>)
```

## SQL Examples

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```

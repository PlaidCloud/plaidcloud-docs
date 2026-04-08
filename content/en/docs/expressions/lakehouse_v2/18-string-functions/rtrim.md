---
title: RTRIM
description: "Learn how to use the RTRIM string function in PlaidCloud Lakehouse. Removes trailing whitespace or specified characters from a string."
---

Removes trailing whitespace or specified characters from a string.

## Analyze Syntax

```python
func.rtrim(<str>)
```

## Analyze Examples

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL Syntax

```sql
RTRIM(<str>)
```

## SQL Examples

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```

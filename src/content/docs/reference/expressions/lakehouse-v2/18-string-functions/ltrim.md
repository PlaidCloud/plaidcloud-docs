---
title: LTRIM
description: "Learn how to use the LTRIM string function in PlaidCloud Lakehouse. Removes leading whitespace or specified characters from a string - with syntax and examples."
---

Removes leading whitespace or specified characters from a string.

## Analyze Syntax

```python
func.ltrim(<str>)
```

## Analyze Examples

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL Syntax

```sql
LTRIM(<str>)
```

## SQL Examples

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```

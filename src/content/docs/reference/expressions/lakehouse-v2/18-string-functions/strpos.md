---
title: STRPOS
description: "Learn how to use the STRPOS string function in PlaidCloud Lakehouse. Returns the position of the first occurrence of a substring. Alias for `LOCATE`."
---

Returns the position of the first occurrence of a substring. Alias for `LOCATE`.

## Analyze Syntax

```python
func.strpos(<str>, <substr>)
```

## Analyze Examples

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL Syntax

```sql
STRPOS(<str>, <substr>)
```

## SQL Examples

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```

---
title: TO_BASE64
---

Converts the string argument to base-64 encoded form and returns the result as a character string.
If the argument is not a string, it is converted to a string before conversion takes place.
The result is NULL if the argument is NULL.

# Analyze Syntax

```python
func.
```

## Analyze Examples
```python
func.
+-----------------+
| func. |
+-----------------+
|              50 |
+-----------------+
```

## SQL Syntax

```sql
TO_BASE64(<v>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<v>`     | The value.  |

## Return Type

`VARCHAR`

## SQL Examples

```sql
SELECT TO_BASE64('abc');
+------------------+
| TO_BASE64('abc') |
+------------------+
| YWJj             |
+------------------+
```
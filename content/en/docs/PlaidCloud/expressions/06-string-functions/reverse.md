---
title: REVERSE
---

Returns the string str with the order of the characters reversed.

# Analyze Syntax

```python
func.reverse(<str>)
```

## Analyze Examples
```python
func.reverse('abc')
+----------------------+
| func..reverse('abc') |
+----------------------+
| cba                  |
+----------------------+
```

## SQL Syntax

```sql
REVERSE(<str>)
```

## Arguments

| Arguments | Description       |
|-----------|-------------------|
| `<str>`   | The string value. |

## Return Type

`VARCHAR`

## SQL Examples

```sql
SELECT REVERSE('abc');
+----------------+
| REVERSE('abc') |
+----------------+
| cba            |
+----------------+
```

---
title: RIGHT
---

Returns the rightmost len characters from the string str, or NULL if any argument is NULL.

# Analyze Syntax

```python
func.right(<str>, <len>)
```

## Analyze Examples
```python
func.right('foobarbar', 4)
+----------------------------+
| func.right('foobarbar', 4) |
+----------------------------+
| rbar                       |
+----------------------------+
```

## SQL Syntax

```sql
RIGHT(<str>, <len>);
```

## Arguments

| Arguments | Description                                              |
|-----------|----------------------------------------------------------|
| `<str>`   | The main string from where the character to be extracted |
| `<len>`   | The count of characters                                  |

## Return Type

`VARCHAR`

## SQL Examples

```sql
SELECT RIGHT('foobarbar', 4);
+-----------------------+
| RIGHT('foobarbar', 4) |
+-----------------------+
| rbar                  |
+-----------------------+
```

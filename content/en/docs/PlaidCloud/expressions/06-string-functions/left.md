---
title: LEFT
---

Returns the leftmost len characters from the string str, or NULL if any argument is NULL.

# Analyze Syntax

```python
func.left(<str>, <len>)
```

## Analyze Examples

```python
func.left('foobarbar', 5)
+---------------------------+
| func.left('foobarbar', 5) |
+---------------------------+
| fooba                     |
+---------------------------+
```

## SQL Syntax

```sql
LEFT(<str>, <len>);
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
SELECT LEFT('foobarbar', 5);
+----------------------+
| LEFT('foobarbar', 5) |
+----------------------+
| fooba                |
+----------------------+
```

---
title: LEFT
---

Returns the leftmost len characters from the string str, or NULL if any argument is NULL.

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

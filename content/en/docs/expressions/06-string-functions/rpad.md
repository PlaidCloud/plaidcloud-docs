---
title: RPAD
---

Returns the string str, right-padded with the string padstr to a length of len characters.
If str is longer than len, the return value is shortened to len characters.

# Analyze Syntax

```python
func.rpad(<str>, <len>, <padstr>)
```

## Analyze Examples
```python
func.rpad('hi',5,'?')
+-----------------------+
| func.rpad('hi',5,'?') |
+-----------------------+
| hi???                 |
+-----------------------+

func.rpad('hi',1,'?')
+-----------------------+
| func.rpad('hi',1,'?') |
+-----------------------+
| h                     |
+-----------------------+
```

## SQL Syntax

```sql
RPAD(<str>, <len>, <padstr>)
```

## Arguments

| Arguments  | Description     |
|------------|-----------------|
| `<str>`    | The string.     |
| `<len>`    | The length.     |
| `<padstr>` | The pad string. |

## Return Type

`VARCHAR`

## SQL Examples

```sql
SELECT RPAD('hi',5,'?');
+--------------------+
| RPAD('hi', 5, '?') |
+--------------------+
| hi???              |
+--------------------+

SELECT RPAD('hi',1,'?');
+--------------------+
| RPAD('hi', 1, '?') |
+--------------------+
| h                  |
+--------------------+
```

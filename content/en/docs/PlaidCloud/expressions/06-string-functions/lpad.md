---
title: LPAD
---

Returns the string str, left-padded with the string padstr to a length of len characters.
If str is longer than len, the return value is shortened to len characters.

# Analyze Syntax

```python
func.lpad(<str>, <len>, <padstr>)
```

## Analyze Examples

```python
func.lpad('hi',4,'??')
+------------------------+
| func.lpad('hi',4,'??') |
+------------------------+
| ??hi                   |
+------------------------+
```

```python
func.lpad('hi',1,'??')
+------------------------+
| func.lpad('hi',1,'??') |
+------------------------+
| h                      |
+------------------------+
```

## SQL Syntax

```sql
LPAD(<str>, <len>, <padstr>)
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
SELECT LPAD('hi',4,'??');
+---------------------+
| LPAD('hi', 4, '??') |
+---------------------+
| ??hi                |
+---------------------+

SELECT LPAD('hi',1,'??');
+---------------------+
| LPAD('hi', 1, '??') |
+---------------------+
| h                   |
+---------------------+
```

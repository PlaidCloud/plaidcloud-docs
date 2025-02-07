---
title: STRCMP
---

Returns 0 if the strings are the same, -1 if the first argument is smaller than the second, and 1 otherwise.

# Analyze Syntax

```python
func.strcmp(<expr1> ,<expr2>)
```

## Analyze Examples
```python
func.strcmp('text', 'text2')
+------------------------------+
| func.strcmp('text', 'text2') |
+------------------------------+
|                           -1 |
+------------------------------+

func.strcmp('text2', 'text')
+------------------------------+
| func.strcmp('text2', 'text') |
+------------------------------+
|                            1 |
+------------------------------+

func.strcmp('text', 'text')
+------------------------------+
| func.strcmp('text', 'text')  |
+------------------------------+
|                            0 |
+------------------------------+
```

## SQL Syntax

```sql
STRCMP(<expr1> ,<expr2>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr1>` | The string. |
| `<expr2>` | The string. |

## Return Type

`BIGINT`

## SQL Examples

```sql
SELECT STRCMP('text', 'text2');
+-------------------------+
| STRCMP('text', 'text2') |
+-------------------------+
|                      -1 |
+-------------------------+

SELECT STRCMP('text2', 'text');
+-------------------------+
| STRCMP('text2', 'text') |
+-------------------------+
|                       1 |
+-------------------------+

SELECT STRCMP('text', 'text');
+------------------------+
| STRCMP('text', 'text') |
+------------------------+
|                      0 |
+------------------------+
```

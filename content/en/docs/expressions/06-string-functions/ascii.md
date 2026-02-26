---
title: ASCII
---

Returns the numeric value of the leftmost character of the string str.

## Analyze Syntax

```python
func.ascii(<expr>)
```

## Analyze Examples
```python
func.ascii('2')
+-----------------+
| func.ascii('2') |
+-----------------+
|              50 |
+-----------------+
```

## SQL Syntax

```sql
ASCII(<expr>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | The string. |

## Return Type

`TINYINT`

## SQL Examples

```sql
SELECT ASCII('2');
+------------+
| ASCII('2') |
+------------+
|         50 |
+------------+
```

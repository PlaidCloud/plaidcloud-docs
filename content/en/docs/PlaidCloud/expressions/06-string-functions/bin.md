---
title: BIN
---

Returns a string representation of the binary value of N.

## Analyze Syntax

```python
func.bin(<expr>)
```

## Analyze Examples
```python
func.bin(12)
+--------------+
| func.bin(12) |
+--------------+
| 1100         |
+--------------+
```

## SQL Syntax

```sql
BIN(<expr>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | The number. |

## Return Type

`VARCHAR`

## SQL Examples

```sql
SELECT BIN(12);
+---------+
| BIN(12) |
+---------+
| 1100    |
+---------+
```

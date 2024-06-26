---
title: ORD
---

If the leftmost character is not a multibyte character, ORD() returns the same value as the ASCII() function.

If the leftmost character of the string str is a multibyte character, returns the code for that character,
calculated from the numeric values of its constituent bytes using this formula:

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

# Analyze Syntax

```python
func.ord(<str>)
```

## Analyze Examples

```python
func.ord('2')
+----------------+
| func.ord('2)   |
+----------------+
|             50 |
+----------------+
```

## SQL Syntax

```sql
ORD(<str>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<str>`   | The string. |

## Return Type

`BIGINT`

## SQL Examples

```sql
SELECT ORD('2')
+--------+
| ORD(2) |
+--------+
|     50 |
+--------+
```

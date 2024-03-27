---
id: string-char
title: CHAR
---

Return the character for each integer passed.

# Analyze Syntax

```python
func.char(N,...)
```

## Analyze Examples
```python
func.char(77,121,83,81,76)
+-----------------------------+
| func.char(77,121,83,81,76) |
+-----------------------------+
| 4D7953514C                  |
+-----------------------------+
```

## SQL Syntax

```sql
CHAR(N, ...)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| N         | Numeric Column |

## Return Type

`BINARY`

## SQL Examples

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```

---
title: UPPER
---

Returns a string with all characters changed to uppercase.

# Analyze Syntax

```python
func.unhex(<expr>)
```

## Analyze Examples
```python
func.upper('hello, plaidcloud lakehouse!')
+--------------------------------------------+
| func.upper('hello, plaidcloud lakehouse!') |
+--------------------------------------------+
| 'HELLO, PLAIDCLOUD LAKEHOUSE!'             |
+--------------------------------------------+
```

## SQL Syntax

```sql
UPPER(<str>)
```

## Aliases

- [UCASE](ucase)

## Return Type

VARCHAR

## SQL Examples

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
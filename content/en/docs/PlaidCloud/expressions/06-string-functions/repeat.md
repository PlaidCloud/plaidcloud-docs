---
title: REPEAT
---

Returns a string consisting of the string str repeated count times. If count is less than 1, returns an empty string. Returns NULL if str or count are NULL.

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
REPEAT(<str>, <count>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<str>`   | The string. |
| `<count>` | The number. |

## SQL Examples

```sql
SELECT REPEAT('databend', 3);
+--------------------------+
| REPEAT('databend', 3)    |
+--------------------------+
| databenddatabenddatabend |
+--------------------------+

SELECT REPEAT('databend', 0);
+-----------------------+
| REPEAT('databend', 0) |
+-----------------------+
|                       |
+-----------------------+

SELECT REPEAT('databend', NULL);
+--------------------------+
| REPEAT('databend', NULL) |
+--------------------------+
|                     NULL |
+--------------------------+
```


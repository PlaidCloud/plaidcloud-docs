---
title: QUOTE
---

Quotes a string to produce a result that can be used as a properly escaped data value in an SQL statement. 

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
QUOTE(<str>)
```

## SQL Examples

```sql
SELECT QUOTE('Don\'t!');
+-----------------+
| QUOTE('Don't!') |
+-----------------+
| Don\'t!         |
+-----------------+

SELECT QUOTE(NULL);
+-------------+
| QUOTE(NULL) |
+-------------+
|        NULL |
+-------------+
```



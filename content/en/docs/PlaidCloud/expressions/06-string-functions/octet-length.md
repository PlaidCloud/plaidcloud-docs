---
title: OCTET_LENGTH
---

OCTET_LENGTH() is a synonym for LENGTH().

# Analyze Syntax

```python
func.octet_length(<str>)
```

## Analyze Examples

```python
func.octet_length('databend')
+-------------------------------+
| func.octet_length('databend') |
+-------------------------------+
|                             8 |
+-------------------------------+
```

## SQL Syntax

```sql
OCTET_LENGTH(<str>)
```

## SQL Examples

```sql
SELECT OCTET_LENGTH('databend');
+--------------------------+
| OCTET_LENGTH('databend') |
+--------------------------+
|                        8 |
+--------------------------+
```



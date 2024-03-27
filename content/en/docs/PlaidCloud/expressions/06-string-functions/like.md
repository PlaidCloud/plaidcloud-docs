---
title: LIKE
---

Pattern matching using an SQL pattern. Returns 1 (TRUE) or 0 (FALSE). If either expr or pat is NULL, the result is NULL.

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
<expr> LIKE <pattern>
```

## SQL Examples

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' ORDER BY name;
+----------+------------+
| name     | category   |
+----------+------------+
| touint16 | conversion |
| touint32 | conversion |
| touint64 | conversion |
| touint8  | conversion |
+----------+------------+
```
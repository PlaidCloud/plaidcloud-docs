---
title: NOT LIKE
---

Pattern not matching using an SQL pattern. Returns 1 (TRUE) or 0 (FALSE). If either expr or pat is NULL, the result is NULL.

## SQL Syntax

```sql
<expr> NOT LIKE <pattern>
```

## SQL Examples

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' AND name not like '%64' ORDER BY name;
+----------+------------+
| name     | category   |
+----------+------------+
| touint16 | conversion |
| touint32 | conversion |
| touint8  | conversion |
+----------+------------+
```
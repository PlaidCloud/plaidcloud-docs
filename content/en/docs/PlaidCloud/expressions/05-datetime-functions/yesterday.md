---
title: YESTERDAY
---

Returns yesterday date, same as `today() - 1`.

## Analyze Syntax

```python
func.yesterday()
```

## Analyze Examples

```python
func.yesterday()
+------------------+
| func.yesterday() |
+------------------+
| 2021-09-02       |
+------------------+
```

## SQL Syntax

```sql
YESTERDAY()
```

## Return Type

`DATE`, returns date in “YYYY-MM-DD” format.

## SQL Examples

```sql
SELECT YESTERDAY();
+-------------+
| YESTERDAY() |
+-------------+
| 2021-09-02  |
+-------------+

SELECT TODAY()-1;
+---------------+
| (TODAY() - 1) |
+---------------+
| 2021-09-02    |
+---------------+
```

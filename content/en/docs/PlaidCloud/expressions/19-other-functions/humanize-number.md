---
title: HUMANIZE_NUMBER
---

Returns a readable number.

## SQL Syntax

```sql
HUMANIZE_NUMBER(x);
```

## Arguments

| Arguments | Description                |
|-----------|----------------------------|
| x         | The numerical size.        |


## Return Type

String.

## SQL Examples

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
+-------------------------+
| HUMANIZE_NUMBER((1000 * 1000)) |
+-------------------------+
| 1 million               |
+-------------------------+
```

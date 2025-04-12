---
title: HUMANIZE_SIZE
---

Returns the readable size with a suffix(KiB, MiB, etc).

## Analyze Syntax

```python
func.humanize_size(x);
```

## Analyze Examples

```python
func.humanize_size(1024 * 1024)
+----------------------------------------+
| func.func.humanize_size((1024 * 1024)) |
+----------------------------------------+
| 1 MiB                                  |
+----------------------------------------+
```

## SQL Syntax

```sql
HUMANIZE_SIZE(x);
```

## Arguments

| Arguments | Description                |
|-----------|----------------------------|
| x         | The numerical size.        |


## Return Type

String.

## SQL Examples

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
+-------------------------+
| HUMANIZE_SIZE((1024 * 1024)) |
+-------------------------+
| 1 MiB                    |
+-------------------------+
```

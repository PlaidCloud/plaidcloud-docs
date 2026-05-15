---
title: TRIM_TRAILING (Lakehouse v1)
description: TRIM_TRAILING — removes all occurrences of the specified trim string from the end of the string.
---

Removes all occurrences of the specified trim string from the end of the string.

See also: 

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Analyze Syntax

```python
func.trim_trailing(<string>, <trim_string>)
```

## Analyze Examples

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## SQL Syntax

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## SQL Examples

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

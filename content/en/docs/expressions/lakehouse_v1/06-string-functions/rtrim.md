---
title: RTRIM
---

Removes all occurrences of any character present in the specified trim string from the right side of the string.

See also: 

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Analyze Syntax

```python
func.rtrim(<string>, <trim_string>)
```

## Analyze Examples

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL Syntax

```sql
RTRIM(<string>, <trim_string>)
```

## SQL Examples

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
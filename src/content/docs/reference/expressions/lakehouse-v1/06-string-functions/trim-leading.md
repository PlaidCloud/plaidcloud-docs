---
title: TRIM_LEADING (Lakehouse v1)
description: TRIM_LEADING — removes all occurrences of the specified trim string from the beginning of the string.
---

Removes all occurrences of the specified trim string from the beginning of the string.

See also: 

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Analyze Syntax

```python
func.trim_leading(<string>, <trim_string>)
```

## Analyze Examples

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## SQL Syntax

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## SQL Examples

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

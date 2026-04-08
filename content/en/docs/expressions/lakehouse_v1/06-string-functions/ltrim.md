---
title: LTRIM
description: "Learn how to use the LTRIM string function in PlaidCloud Lakehouse. Removes all occurrences of any character present in the specified trim string from the..."
---

Removes all occurrences of any character present in the specified trim string from the left side of the string.

See also: 

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Analyze Syntax

```python
func.ltrim(<string>, <trim_string>)
```

## Analyze Examples

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL Syntax

```sql
LTRIM(<string>, <trim_string>)
```

## SQL Examples

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
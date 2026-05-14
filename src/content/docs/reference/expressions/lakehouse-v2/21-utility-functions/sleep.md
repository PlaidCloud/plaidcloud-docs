---
title: SLEEP
description: "Learn how to use the SLEEP utility function in PlaidCloud Lakehouse. Pauses execution for a specified number of seconds. Returns 0 on success."
---

Pauses execution for a specified number of seconds. Returns 0 on success.

## Analyze Syntax

```python
func.sleep(<seconds>)
```

## Analyze Examples

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## SQL Syntax

```sql
SLEEP(<seconds>)
```

## SQL Examples

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```

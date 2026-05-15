---
title: CURTIME (Lakehouse v2)
description: CURTIME — returns the current time. Alias for `CURRENT_TIME`.
---

Returns the current time. Alias for `CURRENT_TIME`.

## Analyze Syntax

```python
func.curtime()
```

## Analyze Examples

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL Syntax

```sql
CURTIME()
```

## SQL Examples

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```

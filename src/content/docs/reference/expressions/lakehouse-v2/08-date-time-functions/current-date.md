---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE — returns the current date. Alias for `CURDATE`.
---

Returns the current date. Alias for `CURDATE`.

## Analyze Syntax

```python
func.current_date()
```

## Analyze Examples

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL Syntax

```sql
CURRENT_DATE()
```

## SQL Examples

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

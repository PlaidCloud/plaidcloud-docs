---
title: INSPECT_ALL_PIPES (Lakehouse v2)
description: INSPECT_ALL_PIPES — returns information about all pipe objects.
---

Returns information about all pipe objects.

## Analyze Syntax

```python
func.inspect_all_pipes()
```

## Analyze Examples

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## SQL Syntax

```sql
INSPECT_ALL_PIPES()
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```

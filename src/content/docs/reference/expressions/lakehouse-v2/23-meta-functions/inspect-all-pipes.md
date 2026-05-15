---
title: INSPECT_ALL_PIPES
description: INSPECT_ALL_PIPES — returns information about all pipe objects - see syntax, examples, and output.
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

---
title: INSPECT_MEMORY_DETAIL (Lakehouse v2)
description: INSPECT_MEMORY_DETAIL — Returns detailed memory usage information.
---

Returns detailed memory usage information.

## Analyze Syntax

```python
func.inspect_memory_detail()
```

## Analyze Examples

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## SQL Syntax

```sql
INSPECT_MEMORY_DETAIL()
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```

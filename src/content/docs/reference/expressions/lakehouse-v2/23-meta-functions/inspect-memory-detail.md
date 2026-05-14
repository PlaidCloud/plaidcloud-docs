---
title: INSPECT_MEMORY_DETAIL
description: "Learn how to use the INSPECT_MEMORY_DETAIL meta function in PlaidCloud Lakehouse. Returns detailed memory usage information - with syntax and examples."
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

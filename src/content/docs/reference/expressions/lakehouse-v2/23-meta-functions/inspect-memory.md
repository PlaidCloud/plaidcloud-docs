---
title: INSPECT_MEMORY
description: INSPECT_MEMORY — Returns memory usage information for the current node.
---

Returns memory usage information for the current node.

## Analyze Syntax

```python
func.inspect_memory()
```

## Analyze Examples

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## SQL Syntax

```sql
INSPECT_MEMORY()
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```

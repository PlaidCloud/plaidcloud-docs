---
title: INSPECT_MEMORY
description: "Learn how to use the INSPECT_MEMORY meta function in PlaidCloud Lakehouse. Returns memory usage information for the current node - with syntax and examples."
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

---
title: PERCENTILE_EMPTY
description: PERCENTILE_EMPTY — returns an empty percentile state for initialization.
---

Returns an empty percentile state for initialization.

## Analyze Syntax

```python
func.percentile_empty()
```

## Analyze Examples

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## SQL Syntax

```sql
PERCENTILE_EMPTY()
```

## SQL Examples

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```

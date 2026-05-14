---
title: PERCENTILE_EMPTY
description: "Learn how to use the PERCENTILE_EMPTY percentile function in PlaidCloud Lakehouse. Returns an empty percentile state for initialization."
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

---
title: CURRENT_VERSION
description: CURRENT_VERSION — returns the current version of StarRocks - see syntax, examples, and output.
---

Returns the current version of StarRocks.

## Analyze Syntax

```python
func.current_version()
```

## Analyze Examples

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## SQL Syntax

```sql
CURRENT_VERSION()
```

## SQL Examples

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```

---
title: VERSION (Lakehouse v2)
description: VERSION — returns the MySQL protocol version of StarRocks.
---

Returns the MySQL protocol version of StarRocks.

## Analyze Syntax

```python
func.version()
```

## Analyze Examples

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## SQL Syntax

```sql
VERSION()
```

## SQL Examples

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```

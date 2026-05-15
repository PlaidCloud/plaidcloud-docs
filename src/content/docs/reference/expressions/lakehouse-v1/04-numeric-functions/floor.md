---
title: FLOOR (Lakehouse v1)
description: FLOOR — rounds the number down.
---

Rounds the number down.

## Analyze Syntax

```python
func.floor( <x> )
```

## Analyze Examples

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## SQL Syntax

```sql
FLOOR( <x> )
```

## SQL Examples

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```

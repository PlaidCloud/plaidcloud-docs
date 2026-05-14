---
title: FLOOR
description: "Learn how to use the FLOOR numeric function in PlaidCloud Lakehouse. Rounds the number down. Includes detailed syntax, examples, and usage reference."
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

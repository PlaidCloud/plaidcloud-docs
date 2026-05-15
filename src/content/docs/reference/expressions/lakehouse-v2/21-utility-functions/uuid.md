---
title: UUID (Lakehouse v2)
description: UUID — returns a random UUID string.
---

Returns a random UUID string.

## Analyze Syntax

```python
func.uuid()
```

## Analyze Examples

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## SQL Syntax

```sql
UUID()
```

## SQL Examples

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```

---
title: UUID
description: "Learn how to use the UUID utility function in PlaidCloud Lakehouse. Returns a random UUID string - see syntax, examples, and output."
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

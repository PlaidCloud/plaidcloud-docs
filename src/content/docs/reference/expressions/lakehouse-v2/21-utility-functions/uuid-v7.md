---
title: UUID_V7
description: "Learn how to use the UUID_V7 utility function in PlaidCloud Lakehouse. Returns a time-ordered UUID v7 string. UUID v7 values are sortable by creation time."
---

Returns a time-ordered UUID v7 string. UUID v7 values are sortable by creation time.

## Analyze Syntax

```python
func.uuid_v7()
```

## Analyze Examples

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## SQL Syntax

```sql
UUID_V7()
```

## SQL Examples

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

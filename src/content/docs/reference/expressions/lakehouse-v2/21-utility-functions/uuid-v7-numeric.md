---
title: UUID_V7_NUMERIC
description: "Use the UUID_V7_NUMERIC utility function in PlaidCloud Lakehouse. Returns a time-ordered UUID v7 as a 128-bit LARGEINT value. UUID v7 values are sortable by."
---

Returns a time-ordered UUID v7 as a 128-bit LARGEINT value. UUID v7 values are sortable by creation time.

## Analyze Syntax

```python
func.uuid_v7_numeric()
```

## Analyze Examples

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## SQL Syntax

```sql
UUID_V7_NUMERIC()
```

## SQL Examples

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

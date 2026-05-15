---
title: YEARWEEK
description: YEARWEEK — returns the year and week number for a date as an integer.
---

Returns the year and week number for a date as an integer.

## Analyze Syntax

```python
func.yearweek(<date>[, <mode>])
```

## Analyze Examples

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## SQL Syntax

```sql
YEARWEEK(<date>[, <mode>])
```

## SQL Examples

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```

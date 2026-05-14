---
title: TO_ISO8601
description: "Learn how to use the TO_ISO8601 date/time function in PlaidCloud Lakehouse. Converts a date or datetime to an ISO 8601 formatted string."
---

Converts a date or datetime to an ISO 8601 formatted string.

## Analyze Syntax

```python
func.to_iso8601(<datetime>)
```

## Analyze Examples

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
TO_ISO8601(<datetime>)
```

## SQL Examples

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```

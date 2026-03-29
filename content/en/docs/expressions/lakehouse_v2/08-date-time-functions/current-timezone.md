---
title: CURRENT_TIMEZONE
---

Returns the current session time zone.

## Analyze Syntax

```python
func.current_timezone()
```

## Analyze Examples

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## SQL Syntax

```sql
CURRENT_TIMEZONE()
```

## SQL Examples

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```

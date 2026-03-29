---
title: JODATIME_FORMAT
---

Formats a date or datetime using Joda-Time format patterns.

## Analyze Syntax

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Analyze Examples

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQL Syntax

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## SQL Examples

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```

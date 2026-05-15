---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — parses a string into a datetime using Joda-Time format patterns.
---

Parses a string into a datetime using Joda-Time format patterns.

## Analyze Syntax

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Analyze Examples

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL Syntax

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## SQL Examples

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```

---
title: TIME_SLOT
---

Rounds the time to the half-hour.

## Analyze Syntax

```python
func.time_slot(<expr>)
```

## Analyze Examples

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## SQL Syntax

```sql
time_slot(<expr>)
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| `<expr>`    | timestamp   |

## Return Type

`TIMESTAMP`, returns in “YYYY-MM-DD hh:mm:ss.ffffff” format.

## SQL Examples

```sql
SELECT
  time_slot('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                │
├─────────────────────────────────────────┤
│ 2023-11-12 09:30:00                     │
└─────────────────────────────────────────┘
```

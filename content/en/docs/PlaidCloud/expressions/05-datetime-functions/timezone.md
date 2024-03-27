---
title: TIMEZONE
---

Returns the timezone for the current connection. 

PlaidCloud Lakehouse uses UTC (Coordinated Universal Time) as the default timezone and allows you to change the timezone to your current geographic location. For the available values you can assign to the `timezone` setting, refer to https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html. See the examples below for details.

## SQL Syntax

```
SELECT TIMEZONE();
```

## SQL Examples

```sql
-- Return the current timezone
SELECT TIMEZONE();
+-----------------+
| TIMEZONE('UTC') |
+-----------------+
| UTC             |
+-----------------+

-- Set the timezone to China Standard Time
SET timezone='Asia/Shanghai';

SELECT TIMEZONE();
+---------------------------+
| TIMEZONE('Asia/Shanghai') |
+---------------------------+
| Asia/Shanghai             |
+---------------------------+
```